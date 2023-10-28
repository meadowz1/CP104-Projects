"""
-------------- ----------------------------------------------------------
Lab 2, Task 8
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = "2023-09-20'
------------------------------------------------------------------------
"""

height = float(input("Enter your height (m): "))
mass = float(input("Enter your weight (kg): "))
upperBMILimit = int(input("Enter your upper limit BMI (23 if you are from South East Asia and Southern China, 25 for everyone else): "))

bmi = mass / (height**2)

bmiPrime = bmi / upperBMILimit

print("Body Mass Index (kg/m^2) = ", bmi)
print("BMI Prime = ", bmiPrime)
