"""
------------------------------------------------------------------------
Lab 2, Task 3
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-09-13'
------------------------------------------------------------------------
"""

# Constants
LARGE_DOG_COST = 75
SMALL_DOG_COST = 50

large_dog_groomed = int(input("Number of large dogs groomed: "))
small_dog_groomed = int(input("Number of small dogs groomed: "))

total_earned = (large_dog_groomed * LARGE_DOG_COST) + (small_dog_groomed * SMALL_DOG_COST)

print("Total earned for the day: $", total_earned)