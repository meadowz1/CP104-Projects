"""
------------------------------------------------------------------------
Assignment 2, Task 2
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-10-07'
------------------------------------------------------------------------
"""

number = int(input("Enter a positive digit number: "))

digit1 = int(number / 10)

digit2 = int(number % 10)

answer = digit1 - digit2

print(f"The difference of the digits of {number} is {answer}")