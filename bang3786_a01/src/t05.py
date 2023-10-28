"""
------------------------------------------------------------------------
Assignment 1, Task 5
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-09-30'
------------------------------------------------------------------------
"""

principal = float(input("Principal: $"))
interest = float(input("Interest (%): "))
years = int(input("Number of years: "))
compounding_amount = int(input("Number of times interest compounded per year: "))

interest_rate = 1 + ((interest/100)/compounding_amount)

amount = principal * (interest_rate**(years*compounding_amount))

print(f"Balance = ${amount}")