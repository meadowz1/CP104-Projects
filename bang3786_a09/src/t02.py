"""
------------------------------------------------------------------------
Assignment 9, Task 2
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-12-02'
------------------------------------------------------------------------
"""

from functions import read_integers

# numbers file original
file = open("numbers.txt", "r", encoding="utf-8")
print(read_integers(file))
print()

# mixed numbers file
file2 = open("numbers2.txt", "r", encoding="utf-8")
print(read_integers(file2))
print()

# empty file
file3 = open("empty.txt", "r", encoding="utf-8")
print(read_integers(file3))
print()