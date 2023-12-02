"""
------------------------------------------------------------------------
Assignment 9, Task 1
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-12-02'
------------------------------------------------------------------------
"""

from functions import file_top

# Printing 5 Lines
file_handle = open("mnm.txt", "r", encoding="utf-8")
file_top(file_handle, 5)

print() 

# Printing No Lines

file_handle = open("mnm.txt", "r", encoding="utf-8")
file_top(file_handle, 0)

print()

# Printing too many lines

file_handle = open("mnm.txt", "r", encoding="utf-8")
file_top(file_handle, 28)

print()