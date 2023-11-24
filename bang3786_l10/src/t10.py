"""
------------------------------------------------------------------------
Lab 10, Task 10
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-11-24'
------------------------------------------------------------------------
"""

from functions import count_frequency_word

fh = open("words.txt", "r", encoding="utf-8")

word = " "

print(count_frequency_word(fh, word))