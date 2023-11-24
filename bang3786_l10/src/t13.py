"""
------------------------------------------------------------------------
Lab 10, Task 13
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-11-24'
------------------------------------------------------------------------
"""

from functions import file_copy

fh = open("words.txt", "r", encoding="utf-8")

fh2 = open("new_words.txt", "w", encoding="utf-8")

file_copy(fh, fh2)