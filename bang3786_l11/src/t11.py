"""
------------------------------------------------------------------------
Lab 11, Task 11
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-12-01'
------------------------------------------------------------------------
"""

from functions import find_word_vertical

matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]
word = "beh"
cols = find_word_vertical(matrix, word)
print(f"Columns with the word '{word}': {cols}")

print()

matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["j", "k", "l"]
]
word = "beh"
cols = find_word_vertical(matrix, word)
print(f"Columns with the word '{word}': {cols}")

print()

matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]
word = "xyz"
cols = find_word_vertical(matrix, word)
print(f"Columns with the word '{word}': {cols}")

print()

matrix = []
word = "abc"
cols = find_word_vertical(matrix, word)
print(f"Columns with the word '{word}': {cols}")

