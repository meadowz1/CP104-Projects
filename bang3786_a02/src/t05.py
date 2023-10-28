"""
------------------------------------------------------------------------
Assignment 2, Task 5
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-10-07'
------------------------------------------------------------------------
"""

foundation_length = float(input("Foundation length (m): "))
foundation_width = float(input("Foundation width (m): "))
foundation_height = float(input("Foundation height (m): "))
wall_height = float(input("Wall height (m): "))
concrete_cost = float(input("Cost of concrete ($/m^3): "))
brick_cost = float(input("Cost of brick ($/m^2): "))

foundation_volume = foundation_height * foundation_length * foundation_width
concrete_final_cost = foundation_volume * concrete_cost

wall_measurements = 2*(wall_height * foundation_length) + 2*(wall_height * foundation_width)
brick_final_cost = wall_measurements * brick_cost

total_cost = brick_final_cost + concrete_final_cost

print(f"""
Concrete needed for foundation (m^3): {foundation_volume:.2f}
Cost of concrete: ${concrete_final_cost:.2f}
Bricks needed for walls (m^2): {wall_measurements:.2f}
Cost of bricks: ${brick_final_cost:.2f}
Total cost: ${total_cost:.2f}
""") 
