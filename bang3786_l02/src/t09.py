"""
------------------------------------------------------------------------
Lab 2, Task 9
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-09-20'
------------------------------------------------------------------------
"""

# Constants
PI = 3.14

diameter = float(input("Diameter of container base (cm): "))
height = float(input("Height of container (cm): "))
costOfMaterial = float(input("Cost of material ($/cm^2): "))
amount = int(input("Number of containers: "))

radius = diameter / 2

areaOfSides = 2 * PI * radius * height
areaOfBase = PI * (radius**2)

totalSurfaceArea = areaOfBase + areaOfBase + areaOfBase

# TODO 

costOfOne = totalSurfaceArea / costOfMaterial
costOfAmount = costOfOne * amount

print("The total cost of one container is $", costOfOne)
print("The total cost of all container is $", costOfAmount)