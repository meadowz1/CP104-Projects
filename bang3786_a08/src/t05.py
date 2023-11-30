"""
------------------------------------------------------------------------
Assignment 8, Task 5
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-11-24'
------------------------------------------------------------------------
"""

from functions import has_word_chain

# Test Case 1
word_chain1 = ["apple", "elephant", "tiger", "rabbit"]
result1 = has_word_chain(word_chain1)
print(result1)  # Output: True

# Test Case 2
word_chain2 = ["python", "node", "elephant", "tiger"]
result2 = has_word_chain(word_chain2)
print(result2)  # Output: False

# Test Case 3
word_chain3 = ["book", "kite", "egg", "giraffe"]
result3 = has_word_chain(word_chain3)
print(result3)  # Output: True
