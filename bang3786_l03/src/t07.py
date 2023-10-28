"""
------------------------------------------------------------------------
Lab 3, Task 7
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-09-29'
------------------------------------------------------------------------
"""

breakfast = float(input("Enter cost of breakfast: $"))
lunch = float(input("Enter cost of lunch: $"))
supper = float(input("Enter cost of supper: $"))

total = breakfast + lunch + supper

print(f"""
Meal         Cost
Breakfast    ${breakfast:6.2f}
Lunch        ${lunch:6.2f}
Supper       ${supper:6.2f}
Total        ${total:6.2f}
""")