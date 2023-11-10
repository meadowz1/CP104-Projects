"""
------------------------------------------------------------------------
Functions for Lab 8
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = "2020-11-"
------------------------------------------------------------------------
"""

from random import randint

# Tasks: 1, 4, 6, 8, 10

# Task 1 Start
def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    name = days[(d-1)]
    
    return name
# Task 1 Finish


# Task 4 Start
def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    
    values = []
    
    for i in range(0, n):
        values.append(randint(low, high))
        i += 0
    
    return values
# Task 4 Finish


# Task 6 Start
def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    
    total = 0.0
    smallest = float(values[0])
    largest = float(values[0])
    values_length = len(values)
    
    for i in range(0, values_length):
        if smallest > values[i]:
            smallest = values[i]
    
    for i in range(0, values_length):
        if largest < values[i]:
            largest = values[i]
    
    for i in range(0, values_length):
        total += values[i]
    
    average = total / values_length
    
    return smallest, largest, total, average
# Task 6 Finish


# Task 8 Start
def linear_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns its index.
    User: index = linear_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        index - the index of the location of value in values,
            -1 if not found (int).
    -------------------------------------------------------
    """
    
    i = 0
    index = -1
    
    while i < len(values):
        if values[i] == value:
            index = i
            i = len(values)
            
        i += 1
        
    return index
# Task 8 Finish


# Task 10 Start
def min_search(values):
    """
    -------------------------------------------------------
    Searches through values for the minimum value(s) and returns a
    list of the indexes of those values. (Assumes values has at least
    one element.)
    User: indexes = min_search(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
    Returns:
        indexes - a list of indexes of the minimum values in
            values (list of int).
    -------------------------------------------------------
    """
    
    min_value = min(values)
    indexes = []
    i = 0
    
    while i < len(values):
        if values[i] == min_value:
            indexes.append(i)
        i += 1
        
    return indexes
        
# Task 10 Finish