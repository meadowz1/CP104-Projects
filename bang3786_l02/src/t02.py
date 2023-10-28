"""
------------------------------------------------------------------------
Lab 2, Task 2
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-09-13'
------------------------------------------------------------------------
"""

# Constants
CF_RATIO = 5/9
FAHRENHEIT_FREEZING = 32

fahrenheit = int(input("Temperature (F): "))

celsius = (fahrenheit - FAHRENHEIT_FREEZING) * CF_RATIO
celsius = str(round(celsius, 1))

print("Temperature (C):", celsius)