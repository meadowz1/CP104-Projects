"""
------------------------------------------------------------------------
Lab 4, Functions
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-10-06'
------------------------------------------------------------------------
"""
from math import sqrt

def diameter(radius):
    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: diam = diameter(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        diam - diameter of a circle (float)
    ------------------------------------------------------
    """
    
    if isinstance(radius, str) == True:
        total = ("please enter a number")
    
    elif radius >= 0:
        total = radius * 2
    
    elif radius < 0:
        total = "input a positive number."
    
    else:
        total = ("input a number.")
        
    return total


def square_pyramid(base, height):
    """
    -------------------------------------------------------
    Calculates and returns the slant height, area, and
    volume of a square pyramid given the base and perpendicular
    height.
    Use: sh, area, vol = square_pyramid(base, height)
    -------------------------------------------------------
    Parameters:
        base - length of the base of the pyramid (float > 0)
        height - perpendicular height of the pyramid (float > 0)
    Returns:
        sh - slant height of the square pyramid (float)
        area - area of the square pyramid (float)
        vol - volume of the square pyramid (float)
    ------------------------------------------------------
    """
    checker = True
    
    if (base >= 0) & (height >= 0):
        base = base
        height = height
    
    else:
        checker = False
        
    if (checker == True):
        sb = base / 2
        basesquare = base**2
        
        sh = sqrt(sb**2 + height**2)
        
        area = basesquare + 2 * base * sqrt((basesquare/4) + height**2)
        
        volume = basesquare * (height/3)
        
    
    else: 
        sh = 0
        area = 0
        volume = 0
        
    return sh, area, volume


def total_change(nickels, dimes, quarters, loonies, toonies):
    """
    -------------------------------------------------------
    Calculates the total value of a set of coins in dollars.
    Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: total = total_change(nickels, dimes, quarters,
        loonies, toonies)
    -------------------------------------------------------
    Parameters:
        nickels - number of nickels (int >= 0)
        dimes - number of dimes (int >= 0)
        quarters - number of quarters (int >= 0)
        loonies - number of loonies (int >= 0)
        toonies - number of toonies (int >= 0)
    Returns:
        total - total value of coins (float)
    -------------------------------------------------------
    """
    
    NICKEL = 0.05
    DIME = 0.10
    QUARTER = 0.25
    LOONIE = 1.00
    TOONIE = 2.00
    
    total = (NICKEL * nickels) + (DIME * dimes) + (QUARTER * quarters) + (LOONIE * loonies) + (TOONIE * toonies)
    
    return total    


def slope(x1, y1, x2, y2):
    """
    -------------------------------------------------------
    Calculates the slope of a line. Slope is calculated as
    rise / run, where rise is distance between y coordinates,
    and run is distance between x coordinates.
    Use: slp = slope(x1, y1, x2, y2)
    -------------------------------------------------------
    Parameters:
        x1 - x coordinate of first point on a graph (float)
        y1 - y coordinate of first point on a graph (float)
        x2 - x coordinate of second point on a graph (float)
        y2 - y coordinate of second point on a graph (float)
        x2 != x1
    Returns:
        slp - slope of the line through (x1,y1) and (x2,y2)
    -------------------------------------------------------
    """
    
    rise = y2 - y1
    run = x2 - x1
    
    total = rise / run
    
    return total


def time_values(seconds):
    """
    -------------------------------------------------------
    Returns seconds in different formats.
    Use: days, hours, minutes = time_values(seconds)
    -------------------------------------------------------
    Parameters:
        seconds - total seconds (int >= 0)
    Returns:
        days - number of days in total_seconds (int >= 0)
        hours - number of hours in total_seconds (int >= 0)
        minutes - number of minutes in total_seconds (int >= 0)
    -------------------------------------------------------
    """
    
    DAY = 86400
    HOUR = 3600
    MINUTE = 60
    
    days = 0
    hours = 0
    minutes = 0
    
    if (seconds < 3600) & (seconds > 0):
        minutes = seconds // MINUTE
        days = 0
        hours = 0
        
    elif (seconds == 3600):
        days = 0
        hours = 1
        minutes = 60
    
    elif (seconds < 86400):
        hours = seconds // HOUR
        minutes = seconds // MINUTE
        days = 0
    
    elif (seconds == 86400):
        days = 1
        hours = 24
        minutes = 1440
    
    else: 
        days = seconds // DAY
        hours = seconds // HOUR
        minutes = seconds // MINUTE
    
    return days, hours, minutes
    
    
    
    