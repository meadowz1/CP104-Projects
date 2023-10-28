"""
------------------------------------------------------------------------
Lab 4, Task 1
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-10-06'
------------------------------------------------------------------------
"""

from functions import time_values

days, hours, minutes = time_values(3600)

print(days, hours, minutes)

days, hours, minutes = time_values(86400)

print(days, hours, minutes)


days, hours, minutes = time_values(6420982)

print(days, hours, minutes)