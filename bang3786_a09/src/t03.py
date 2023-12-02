"""
------------------------------------------------------------------------
Assignment 9, Task 3
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-12-01'
------------------------------------------------------------------------
"""

from functions import file_statistics

# Original File
file = open("addresses.txt", "r", encoding="utf-8")
ucount, lcount, dcount, wcount, rcount = file_statistics(file)
print(f"Upper-case letters: {ucount}")
print(f"Lower-case letters: {lcount}")
print(f"Digits: {dcount}")
print(f"White-space characters: {wcount}")
print(f"Remaining characters: {rcount}")
print()

# Test File with other values
file2 = open("addresses2.txt", "r", encoding="utf-8")
ucount, lcount, dcount, wcount, rcount = file_statistics(file2)
print(f"Upper-case letters: {ucount}")
print(f"Lower-case letters: {lcount}")
print(f"Digits: {dcount}")
print(f"White-space characters: {wcount}")
print(f"Remaining characters: {rcount}")
print()

# Empty File
file3 = open("empty.txt", "r", encoding="utf-8")
ucount, lcount, dcount, wcount, rcount = file_statistics(file3)
print(f"Upper-case letters: {ucount}")
print(f"Lower-case letters: {lcount}")
print(f"Digits: {dcount}")
print(f"White-space characters: {wcount}")
print(f"Remaining characters: {rcount}")