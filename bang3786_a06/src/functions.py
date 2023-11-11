"""
------------------------------------------------------------------------
Assignment 6 Functions
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-11-11'
------------------------------------------------------------------------
"""

# Task 1 Start
def total_wins():
    """
    -------------------------------------------------------
    Calculates the total wins for two teams, 'purple' <str> and
    'gold' <str>. The user enters a series of strings, and once
    they decide to finish, they must press 'Enter' or input
    an empty string on their keyboard. 
    -------------------------------------------------------
    Use: purple, gold = total_wins()
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        purple - <str> number of purple wins
        gold - <str>  number of gold wins
    ------------------------------------------------------
    """
    
    purple = 0 
    gold = 0 
    finish = False
    
    while finish == False:
        team = input("Enter the winning team: ")
        
        if team == "purple":
            purple += 1
        
        elif team == "gold":
            gold += 1
        
        elif team == "":
            finish = True
        
    return purple, gold
# Task 1 Finish



# Task 2 Start
def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    
    prime = False
    i = 2
    
    if number == 1:
        prime = False
    
    elif number > 1:
        while prime == False:
            if (number % i) == 0:
                if number == i:
                    prime = False
                    break
                else:
                    prime = True
                    break
            else:
                i += 1
    return prime
# Task 2 Finish



# Task 3 Start
def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    monthly_interest_rate = interest_rate / 12 / 100
    remaining_principal = principal_amount

    print(f"Principal:   ${principal_amount:.2f}")
    print(f"Interest rate : {interest_rate:.2f}%")
    print(f"Monthly payment: ${payment:.2f}")
    print("----------------------------------")
    print(f"{'Month':<5}{'Interest':>10}{'Payment':>10}{'Balance':>9}")
    print("----------------------------------")

    month = 1
    while remaining_principal > 0:
        monthly_interest = remaining_principal * monthly_interest_rate
        
        if payment >= remaining_principal + monthly_interest:
            payment = remaining_principal + monthly_interest
            
        remaining_principal = max(remaining_principal + monthly_interest - payment, 0)
        
        print(f"{month:>5}{monthly_interest:>8.2f}{payment:>12.2f}{remaining_principal:>9.2f}")

        month += 1
        
    return
# Task 3 Finish



# Task 4 Start
def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    
    digits = 0
    
    while number != 0:
        number = number // 10
        digits += 1
        
    return digits
# Task 4 Finish



# Task 5 Start
def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    total = 0
    i = 1

    while i <= (number // 2):
        
        if number % i == 0:
            total += i
            
        i += 1

    return total
# Task 5 Finish

