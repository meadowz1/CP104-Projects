"""
------------------------------------------------------------------------
Lab 2, Task 1
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-09-13'
------------------------------------------------------------------------
"""

# Constants
FC_RATIO = 9/5
FAHRENHEIT_FREEZING = 32

celsius = int(input("Temperature (C): "))

fahrenheit = FC_RATIO * int(celsius) + FAHRENHEIT_FREEZING
fahrenheit = str(round(fahrenheit, 1))

print("Temperature (F):", fahrenheit)