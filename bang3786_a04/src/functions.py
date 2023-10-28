"""
------------------------------------------------------------------------
Functions Assignment 4
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-10-28'
------------------------------------------------------------------------
"""

# Task 1 Start
def day_name(day_num):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is "Sunday", day 7 is "Saturday".
    Returns "Error" if the number is not valid.
    Use: day = day_name(day_num)
    -------------------------------------------------------
    Parameters:
        day_num - day number (1 <= int <= 7)
    Returns:
        day - name of a day of the week (str)
    ------------------------------------------------------
    """
    
    day = ""

    if day_num == 1:
        day = "Sunday"
    
    elif day_num == 2:
        day = "Monday"
    
    elif day_num == 3:
        day = "Tuesday"
    
    elif day_num == 4:
        day = "Wednesday"
    
    elif day_num == 5:
        day = "Thursday"
    
    elif day_num == 6:
        day = "Friday"
    
    elif day_num == 7:
        day = "Saturday"
    
    else: 
        day = "Error"
    
    return day
# Task 1 End


# Task 2 Start
def pollution_ranking(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if air_quality_index is negative.
    Use: pollution = pollution_ranking(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """
    pollution = " "
    
    if air_quality_index < 0:
        pollution = "Error"
    
    elif air_quality_index > 300:
        pollution = "Hazardous"
    
    elif 0 < air_quality_index <= 50: 
        pollution = "Good"
        
    elif 50 < air_quality_index <= 100:
        pollution = "Moderate"
    
    elif 100 < air_quality_index <= 150:
        pollution = "Unhealthy for Sensitive Groups"
    
    elif 150 < air_quality_index <= 200:
        pollution = "Unhealthy"
    
    elif 200 < air_quality_index <= 300:
        pollution = "Very Unhealthy"
        
    else: 
        pollution = "Error"
        
    return pollution
# Task 2 End


# Task 3 Start
def largest_average(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the average of the two largest values of
    val1, val2, and val3.
    Use: average = largest_average(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        average - the average of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    
    average = 0.0
    
    largest = max(val1, val2, val3)
    
    if largest == val1:
        secondLargest = max(val2, val3)
        
        if secondLargest == val2:
            average = (val1 + val2) / 2
        else:
            average = (val1 + val3) / 2
            
    elif largest == val2:
        secondLargest = max(val1, val3)
        
        if secondLargest == val1:
            average = (val1 + val2) / 2
        else:
            average = (val2 + val3) / 2
            
    else:
        secondLargest = max(val1, val2)
        
        if secondLargest == val1:
            average = (val1 + val3) / 2
        else:
            average = (val2 + val3) / 2
            
    return average
# Task 3 End


# Task 4 Start
def colour_combine(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_combine(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """
    rgb_colour = ""
    
    if (rgb_colour1 == "red") & (rgb_colour2 == "red"): 
        rgb_colour = "red"
    
    elif (rgb_colour1 == "blue") & (rgb_colour2 == "blue"): 
        rgb_colour = "blue"
    
    elif (rgb_colour1 == "green") & (rgb_colour2 == "green"): 
        rgb_colour = "green"
        
    elif ((rgb_colour1 == "red") & (rgb_colour2 == "blue")) | ((rgb_colour1 == "blue") & (rgb_colour2 == "red")): 
        rgb_colour = "fuchsia"
        
    elif ((rgb_colour1 == "red") & (rgb_colour2 == "green")) | ((rgb_colour1 == "green") & (rgb_colour2 == "red")): 
        rgb_colour = "yellow"
        
    elif ((rgb_colour1 == "blue") & (rgb_colour2 == "green")) | ((rgb_colour1 == "green") & (rgb_colour2 == "blue")): 
        rgb_colour = "aqua"
    
    else:
        rgb_colour = "Error"
        
    return rgb_colour
# Task 4 End


# Task 5 Start
def hoo_rah(number):
    """
    -------------------------------------------------------
    Takes an integer parameter and returns one of the following:
        "Hoo" if number is evenly divisible by 2
        "Rah" if number is evenly divisible by 7
        "Hoo Rah" if number is evenly divisible by both 2 and 7
        "Zip" if the number is none of the above.
    Use: hoo_rah = hoo_rah(number)
    -------------------------------------------------------
    Parameters:
        number - an integer value (int)
    Returns:
        hoo_rah - A result from above (str)
    -------------------------------------------------------
    """
    final_value = ""
    
    number_by_2 = number % 2
    number_by_7 = number % 7
    
    if (number_by_2 == 0) & (number_by_7 == 0):
        final_value = "Hoo Rah"
    
    elif (number_by_2 == 0) & (number_by_7 != 0):
        final_value = "Hoo"
    
    elif (number_by_2 != 0) & (number_by_7 == 0):
        final_value = "Rah"
    
    else:
        final_value = "Zip"
        
    return final_value
# Task 5 End
