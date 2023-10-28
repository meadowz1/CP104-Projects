"""
------------------------------------------------------------------------
Lab 4, Task 4
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-10-06'
------------------------------------------------------------------------
"""

from functions import square_pyramid

sh, area, volume = square_pyramid(0, 10)

print(sh, area, volume)

print("")

sh, area, volume = square_pyramid(10, 15)

print(sh, area, volume)

print("")

sh, area, volume = square_pyramid(25, -12)

print(sh, area, volume)

print("")