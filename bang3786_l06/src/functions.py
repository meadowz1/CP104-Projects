"""
------------------------------------------------------------------------
Functions
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-10-27'
------------------------------------------------------------------------
"""

# Task 1 Start
def sum_even(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all even numbers from 2 to num (int)
    ------------------------------------------------------
    """
    total = 0
    
    for i in range(0, num + 1, 2):
        total = total + i
    
    return total

# Task 1 End


# Task 5 Start
def draw_rectangle(height, width, char):
    """
    -------------------------------------------------------
    Prints a rectangle of height and width characters using
    the char character.
    Use: draw_rectangle(height, width, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------
    """
    
    string = ""
    
    for j in range(width):
        string += char
        
    for k in range(height):
        print(string)
        
    return
    
# Task 5 End


# Task 9 Start
def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    
    for i in range(n, 1, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")       
        print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.")       
        print(" ")
        
    print(f"1 bottle of beer on the wall, 1 bottle of beer.")       
    print(f"Take one down, pass it around, no more bottles of beer on the wall!")       
    print(" ")
        
    return
# Task 9 End


# Task 10 Start
def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    
    for i in range(start, end + 1, inc):
        total_burned = i * burnt_per_minute
        print(f"Calories burnt after {i} minutes: {total_burned}")
        
    return
# Task 10 End


# Task 11 Start (not a part of the submissions)
def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    
    RETIRE = 65
    
    salary_increase = increase / 100
    
    print(f"Age{'Salary':>15s}")
    print(f"{'-':-^18s}")

    for i in range(age, RETIRE + 1):
        formatted_salary = "{:,.2f}".format(salary)
        print(f"{i}{formatted_salary:>16s}")
        salary += salary * salary_increase

    return
    
# Task 11 End


# Task 12 Start
def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """
    
    final_value = 0
    print(f"Year{'Value $':>14s}")
    print(f"{'-':-^18s}")
    
    for i in range(0, years, 1):
        formatted_value = "{:,.2f}".format(value)
        print(f"{i:2d}{formatted_value:>16s}")
        value *= (1 + rate / 100) 
        
    formatted_value2 = "{:,.2f}".format(value)
    print(f"{years:2d}{formatted_value2:>16s}")
    final_value = value
    
    return final_value
# Task 12 End

# Task 15 Start
def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    total = 0
    minimum = float('inf')
    maximum = float('-inf')
    
    for i in range(n): 
        value = float(input("Enter a value: ")) 
        total += value
        minimum = min(minimum, value)
        maximum = max(maximum, value)
        
    average = total / n

    return minimum, maximum, total, average
    
# Task 15 End 