"""
------------------------------------------------------------------------
Assignment 3 Functions
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-10-21'
------------------------------------------------------------------------
"""

ACRE = 43560
GRAVITY = 9.8

# Task 1 Start
def footage_to_acres(square_feet):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = footage_to_acres(square_feet)
    -------------------------------------------------------
    Parameters:
        square_feet - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    
    acres = 0
    
    if (square_feet >= 0):
        acres = square_feet / ACRE
    else:
        acres
        
    return acres

# Task 1 Finish


# Task 2 Start
def lawn_mow_time(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = lawn_mow_time(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time_minutes - time required to mow the lawn (float)
    ------------------------------------------------------
    """
    
    time_minutes = (length * width) / speed
    
    return time_minutes
    
# Task 2 Finish


# Task 3 Start
def extract_date(date_number):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format YYYYMMDD.
    Use: year, month, day = extract_date(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format YYYYMMDD (int)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    day = date_number % 100

    month = ((date_number % 10000) - day) // 100

    year = date_number // 10000
    
    return year, month, day

# Task 3 Finish


# Task 4 Start
def multiply_fractions(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = multiply_fractions(num1, den1, num2, den2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of first fraction (int)
        den1 - denominator of first fraction (int != 0)
        num2 - numerator of second fraction (int)
        den2 - denominator of second fraction (int != 0)
    Returns:
        num - numerator of product (int)
        den - denominator of product (int)
        product - num / den (float)
    -------------------------------------------------------
    """
    
    num = num1 * num2
    den = den1 * den2
    product = num / den
    
    return num, den, product

# Task 4 Finish


# Task 5 Start
def falling_distance(falling_time):
    """
    -------------------------------------------------------
    Calculates distance an object has fallen due to gravity given
    the time it is fallen.
    Use: distance = falling_distance(falling_time)
    -------------------------------------------------------
    Parameters:
        falling_time - time object has fallen in seconds (int >= 0)
    Returns:
        distance - distance object has fallen in metres (float)
    -------------------------------------------------------
    """
    
    distance = (GRAVITY * (falling_time ** 2)) * 0.5
    return distance

# Task 5 Finish