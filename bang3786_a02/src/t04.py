"""
------------------------------------------------------------------------
Assignment 2, Task 4
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-10-07'
------------------------------------------------------------------------
"""

flyers = int(input("Number of flyers: "))
people = int(input("Number of delivery people: "))

flyers_per_person = int(flyers/people)
flyers_left_over = flyers % people

print(f"""
Flyers per delivery person: {flyers_per_person}
Flyers left over: {flyers_left_over}
""")