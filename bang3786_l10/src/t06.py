"""
------------------------------------------------------------------------
Lab 10, Task 6
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-11-24'
------------------------------------------------------------------------
"""

from functions import number_stats

fh = open("numbers.txt", "r", encoding="utf-8")

print(number_stats(fh))