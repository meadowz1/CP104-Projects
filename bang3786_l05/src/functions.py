"""
------------------------------------------------------------------------
Functions
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-10-20'
------------------------------------------------------------------------
"""

# Task 1
def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """
    magic = False
    
    magicNum = day * month
    
    if (magicNum == year): 
        magic = True
        
    else:
        magic
        
    return magic
# end of Task 1


# Task 4
def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    
    distanceV1 = abs(target - v1)
    distanceV2 = abs(target - v2)
    closerValue = 0
    
    if (distanceV1 > distanceV2):
        closerValue = v2
    else :
        closerValue = v1
    
    return closerValue
# end of Task 4


# Task 8
def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n is not
          between 1 and 10 inclusive. (str)
    -------------------------------------------------------
    """
    one = "I"
    five = "V"
    ten = "X"
    output = ""
    
    if (n == 1):
        output = one
        
    elif (n == 2):
        output = f"{one}{one}"
    
    elif (n == 3):
        output = f"{one}{one}{one}"
    
    elif (n == 4):
        output = f"{one}{five}"
        
    elif (n == 5):
        output = f"{five}"
    
    elif (n == 6):
        output = f"{five}{one}"
        
    elif (n == 7):
        output = f"{five}{one}{one}"
        
    elif (n == 8):
        output = f"{five}{one}{one}{one}"
        
    elif (n == 9):
        output = f"{one}{ten}"
        
    else:
        output = f"{ten}"
        
    return output
# end of Task 8


# Task 12
def pay_raise(status, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time greater than or equal to 10 years service
        1.5% for full time less than 4 years service
        3% for part time greater than 10 years service
        1% for part time less than 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """
    # Raise Percents
    FULLTIME4 = 0.015
    FULLTIME10 = 0.05
    PARTTIME4 = 0.01
    PARTTIME10 = 0.03
    GENERAL = 0.02
    
    newSalary = 0.0
    
    if status == ("F"):
        if years < 4:
            newSalary = salary + (salary * FULLTIME4)
        elif years >= 10:
            newSalary = salary + (salary * FULLTIME10)
        else:
            newSalary = salary + (salary * GENERAL)
    
    else:
        if years < 4:
            newSalary = salary + (salary * PARTTIME4)
        elif years > 10:
            newSalary = salary + (salary * PARTTIME10)
        else: 
            newSalary = salary + (salary * GENERAL)
        
    return newSalary
# end of Task 12


# Task 14

def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    
    age = int(input("How old are you? "))
    price = 0.0
    
    INFANTAGE = 3
    SENIORAGE = 65
    STUDENTAGELOW = 10
    STUDENTAGEHIGH = 18
    ADULTAGELOW = 18
    ADULTAGEHIGH = 65
    
    INFANT = 0.00
    SENIOR = 4.00
    STUDENTSCHOOL = 1.00
    STUDENT = 3.00
    ADULT = 5
    KID = 2
    
    if age < INFANTAGE:
        price = INFANT
    
    elif age >= SENIORAGE:
        price = SENIOR
        
    elif STUDENTAGELOW <= age < STUDENTAGEHIGH:
        student = input("Are you a student? (enter 'Y' for yes, 'N' for no.): ")
        if student == "Y":
            price = STUDENTSCHOOL
        else:
            price = STUDENT
            
    elif ADULTAGELOW <= age < ADULTAGEHIGH:
        price = ADULT
    
    else:
        price = KID
    
    return price        
# end of Task 14