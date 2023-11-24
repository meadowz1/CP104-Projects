"""
------------------------------------------------------------------------
Lab 10, Task 5
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-11-24'
------------------------------------------------------------------------
"""

from functions import customer_append

fh = open("customers.txt", "a", encoding="utf-8")

fields = ['21211', 'Mike', 'Bangar', 142.69, '2005-05-29']

customer_append(fh, fields)

