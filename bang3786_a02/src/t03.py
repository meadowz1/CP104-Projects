"""
------------------------------------------------------------------------
Assignment 2, Task 3
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-10-07'
------------------------------------------------------------------------
"""

date = int(input("Enter a date in the format YYYYMMDD: "))

year = (date // 10000)

month = (date // 100) - (year * 100)

day = int(date % 100)

print(f"The reformatted date: {year:4d}/{month:0>2d}/{day:0>2d}")