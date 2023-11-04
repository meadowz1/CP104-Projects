"""
------------------------------------------------------------------------
Assignment 5 Functions
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-11-04'
------------------------------------------------------------------------
"""
from _tracemalloc import stop

# Task 1 Start
def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    
    product = 1
        
    for i in range(1, number + 1):
        product = product * i
    
    return product
# Task 1 Finish



# Task 2 Start
def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Calculates how many calories are burned per minute for the given time.
    Use: calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - number of calories burned in a minute (float)
        minutes - amount of time in minutes (int)
    Returns:
        None
    ------------------------------------------------------
    """
    
    for i in range(5, minutes + 1, 5):
        burned = per_min * i
        print(f"{i:>3d}   {burned:>4.1f}")
        
    return

# Task 2 Finish



# Task 3 Start
def arrow_up(rows):
    """
    -------------------------------------------------------
    Takes an integer parameter and prints an arrow made
    from "#" characters pointing upwards. 
    Use: arrow_up(rows)
    ------------------------------------------------------
    Parameters:
        rows - the amount of rows needed to print (int)
    Returns:
        None
    -------------------------------------------------------
    """
    
    for i in range(1, rows +1):
        
        if i == 1:
            print((rows-i) * " " + "#")
        else:
            print((rows-i) * " ", end = "")
            print("#", end = "")
            print((2*i-3) * " ", end = "")
            print("#")
    return
# Task 3 Finish



# Task 4 Start
def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    
    for i in range(start_num, stop_num + 1):
        print(f"{i:>4}", end="")
    print("\n    " + "-" * 22)

    # Print the multiplication table
    for i in range(start_num, stop_num + 1):
        print(f"{i:2} |", end="")
        for j in range(start_num, stop_num + 1):
            product = i * j
            print(f"{product:4}", end="")
        print()
        
    return
# Task 4 Finish



# Task 5 Start
def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
        
    
    for i in range(count):
        total += start
        start += increment
        
    return total
# Task 5 Finish