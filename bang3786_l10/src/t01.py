"""
------------------------------------------------------------------------
Lab 10, Task 1
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-11-24'
------------------------------------------------------------------------
"""

from functions import customer_record

fh = open("customers.txt", "r", encoding="utf-8")

print(customer_record(fh, 9))