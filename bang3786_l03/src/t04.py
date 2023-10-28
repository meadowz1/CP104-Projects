"""
------------------------------------------------------------------------
Lab 3, Task 4
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-09-29'
------------------------------------------------------------------------
"""

dollars = float(input("Enter number: "))

percent = float(input("Enter percent: "))

discount = dollars * (percent/100)

print(f'A {percent:.1f} percent discount on {dollars:.1f} is {discount:.1f}')