"""
------------------------------------------------------------------------
Assignment 9, Task 4
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-12-02'
------------------------------------------------------------------------
"""

from functions import line_numbering

fileread = open("wilde.txt", "r", encoding="utf-8")
filewrite = open("wildewrite.txt", "w", encoding="utf-8")
line_numbering(fileread, filewrite)
print("Success")
print()

fileread2 = open("wilde2.txt", "r", encoding="utf-8")
filewrite2 = open("wildewrite2.txt", "w", encoding="utf-8")
line_numbering(fileread2, filewrite2)
print("Success")
print()

fileread3 = open("empty.txt", "r", encoding="utf-8")
filewrite3 = open("wildewrite3.txt", "w", encoding="utf-8")
line_numbering(fileread3, filewrite3)
print("Success")
print()