"""
------------------------------------------------------------------------
Functions Assignment 7
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = "2020-04-20"
------------------------------------------------------------------------
"""

# Task 1 Start
def list_factors(number):
    """
    -------------------------------------------------------
    Takes an integer greater than 0 as a parameter and returns 
    a list of its factors, excluding the number itself.
    Use: list = list_factors(number)
    -------------------------------------------------------
    Parameters:
    - number (int): The integer for which to find the factors. 
      It should be greater than 0.
    Returns:
    - factors (list): A list of factors for which the number 
      corresponds with. It should have at least 2 numbers.
    -------------------------------------------------------
    """
    factors = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    return factors
# Task 1 End

# Task 2 Start
def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    
    number_list = []
    using = True
    
    while using:
        number = int(input("Enter a positive number: "))
        if number > 0:
            number_list.append(number)
        
        if number == 0:
            using = False
            
    return number_list
# Task 2 End

# Task 3 Start
def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index_list = [i for i, num in enumerate(numbers) if num == target_number]
    
    return index_list
# Task 3 End 

# extra functions
def find_indexes(lst, values):
    """
    Find indexes of values in a list.
    -------------------------------------------------------
    Parameters:
        lst - a list of values (list)
        values - a list of values to find indexes for (list)
    Returns:
        List of indexes of values in the list.
    -------------------------------------------------------
    """
    return [i for i, x in enumerate(lst) if x in values]
# end of extra functions

# Task 4 Start
def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    
    indexes_to_remove = find_indexes(minuend, subtrahend)
    
    for index in sorted(indexes_to_remove, reverse=True):
        del minuend[index]
            
    return
# Task 4 End

# Task 5 Start
def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    n = len(numbers)
    in_order = True
    index = -1
    
    if n <= 1:
        in_order = True
        index = -1

    ascending = numbers[0] <= numbers[1]

    for i in range(1, n):
        if (ascending and numbers[i - 1] > numbers[i]) or (not ascending and numbers[i - 1] < numbers[i]):
            index = i - 1
            in_order = False

    return in_order, index
# Task 5 End