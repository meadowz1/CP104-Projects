"""
------------------------------------------------------------------------
Lab 11, Task 10
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-12-01'
------------------------------------------------------------------------
"""

from functions import find_word_horizontal

matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]
word = "def"
rows = find_word_horizontal(matrix, word)
print(f"Rows with the word '{word}': {rows}")

print()

matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["d", "e", "f"]
]
word = "def"
rows = find_word_horizontal(matrix, word)
print(f"Rows with the word '{word}': {rows}")

print()

matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]
word = "xyz"
rows = find_word_horizontal(matrix, word)
print(f"Rows with the word '{word}': {rows}")


print()

matrix = []
word = "abc"
rows = find_word_horizontal(matrix, word)
print(f"Rows with the word '{word}': {rows}")
