"""
------------------------------------------------------------------------
Lab 2, Task 5
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-09-18'
------------------------------------------------------------------------
"""

hourly_pay = float(input("Hourly rate of pay: $"))
hours_worked = float(input("Hours worked in the week: "))

week_payout = hourly_pay * hours_worked 
week_payout = str(round(week_payout, 2))

print("Total pay for the week: $", week_payout)