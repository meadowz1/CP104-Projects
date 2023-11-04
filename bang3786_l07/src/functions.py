"""
------------------------------------------------------------------------
Functions
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = "2020-04-20"
------------------------------------------------------------------------
"""

from random import randint

# Task 1 Start
def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)
    count = 0
    found = False
    
    while (found == False):
        guess = int(input("Guess: "))
        count +=1
        if guess == number:
            print("Congratulations - good guess!")
            found = True
            
        elif guess < number:
            print("Too low, try again.")
        
        elif guess > number:
            print("Too high, try again.")
            
        else:
            print("Please enter a number.")
        
    print(f"You made {count} guesses.")
    
    return count
    
# Task 1 Finish



# Task 2 Start
def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """

    power = 1
    while power < target:
        power = power * 2
    
    return power
# Task 2 Finish 



# Task 4 Start
def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    
    value = 1
    final = 0
    
    while final <= target:
        final += (value ** 2)
        value += 1
        
    return final
# Task 4 Finish


# Task 7 Start
def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    
    
    print("For Day 1")
    print("")
    b_total = float(input("How much was breakfast? $"))
    l_total = float(input("How much was lunch? $"))
    s_total = float(input("How much was supper? $"))
    a_total = b_total + l_total + s_total
    print(b_total, l_total, s_total, a_total)
    
    counter = 1
    
    print(f"Your total for the day was ${a_total}")
    print("")
    plusday = input("Were you away another day (Y/N)? ")
    
    while plusday == 'Y':
        counter += 1
        print("")
        print(f"For Day {counter}")
        print("")
        b_hold = float(input("How much was breakfast? $"))
        l_hold = float(input("How much was lunch? $"))
        s_hold = float(input("How much was supper? $"))
        a_hold = b_hold + l_hold + s_hold
        formatted_a_hold = "{:,.2f}".format(a_hold)
        print(f"Your total for the day was ${formatted_a_hold}")
        print("")
        b_total = b_total + b_hold
        l_total = l_total + l_hold
        s_total = s_total + s_hold
        a_total = a_total + float(formatted_a_hold)
        print(b_total, l_total, s_total, a_total)
        plusday = input("Were you away another day (Y/N)? ")
        
        
    return (b_total, l_total, s_total, a_total)
# Task 7 Finish



# Task 10 Start
def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    
    OVERTIME = 40
    OVERTIME_RATE = 1.5
    TAX = 0.03625
    
    finish = False
    employee_id = 1
    total = 0.0
    average = 0.0
    employees = 0
    
    while finish == False:
        employee_id = int(input("Employee ID: "))
        
        if employee_id == 0:
            finish = True
            
        else: 
            hourly_wage_rate = int(input("Hourly wage rate: "))
            hours_worked = int(input("Hours worked: "))
            
            if hours_worked <= 40:
                net_pay = hours_worked * hourly_wage_rate
                net_pay = net_pay - (net_pay * TAX)
                total += net_pay
            
            else:
                net_pay = (OVERTIME * hourly_wage_rate) + (((hours_worked - OVERTIME) * hourly_wage_rate) * OVERTIME_RATE)
                net_pay = net_pay - (net_pay * TAX)
                total += net_pay
        
            employees += 1
            print(f"Net payment for employee {employee_id}: ${net_pay:.2f}")
    
    if total > 0:
        average = total / employees
        
    else: 
        total = 0.00
        average = 0.00
    
    return total, average

# Task 10 Finish