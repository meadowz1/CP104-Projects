"""
------------------------------------------------------------------------
Lab 2, Task 6
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-09-18'
------------------------------------------------------------------------
"""

MONTHSINYEARS = 12.0

principal = int(input("Mortgage principal ($): "))
numberofyears = float(input("Number of years: "))
yearlyrate = float(input("Yearly interest rate (%): "))

yearlyrate = yearlyrate / 100
numberofmonths = numberofyears * MONTHSINYEARS
monthlyrate = yearlyrate / MONTHSINYEARS

interest_rate1 = (1.0 + monthlyrate)**numberofmonths
interest_rate2 = monthlyrate * interest_rate1

division = (interest_rate2)/(interest_rate1 - 1)

monthlypayment = (principal)*(division)

print("The monthly payment are: $", monthlypayment)