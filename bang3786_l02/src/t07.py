"""
------------------------------------------------------------------------
Lab 2, Task 7
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-09-18'
------------------------------------------------------------------------
"""

numberofflyers = int(input("Number of flyers: "))
numberofvolunteers= int(input("Number of volunteers: "))

flyerspervolunteer = numberofflyers // numberofvolunteers
flyersleftover = numberofflyers % numberofvolunteers

print("Flyers per volunteer: ", flyerspervolunteer)
print("Flyers left over: ", flyersleftover)
