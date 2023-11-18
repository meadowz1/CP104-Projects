"""
------------------------------------------------------------------------
Lab 9 Functions
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-11-17'
------------------------------------------------------------------------
"""

# Tasks: 1, 3, 4, 5, 10

# Task 1 Start
def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Parameters:
        chemical - a chemical formula (str)
    Returns:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """
    
    hydroxide = chemical.endswith("OH")
    
    return hydroxide
# Task 1 End

# Task 3 Start
def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:]
    
    return pc, pi, pq
    
# Task 3 End

# Task 4 Start
def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: category, digits, qualifiers = validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        category - True if three upper-case characters, False otherwise
        digits - True if four digits, False otherwise
        qualifiers - True if starts with 1 upper-case letter, False otherwise
    -------------------------------------------------------
    """
    
    category = product_code[:3]
    digits = product_code[3:7]
    qualifiers = product_code[7:]

    category_valid = category.isalpha() and category.isupper() and len(category) == 3
    digits_valid = digits.isdigit() and len(digits) == 4
    qualifiers_valid = qualifiers[0].isupper() if qualifiers else False

    return category_valid, digits_valid, qualifiers_valid
# Task 4 End

# Task 5 Start
def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: password_strength(password)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """
    
    numberCount = 0
    upperCase = 0
    lowerCase = 0
    i = 0
    
    if len(password) < 8:
        print("not long enough")
        
    while i < len(password):
        if password[i].isdigit():
            numberCount += 1
        
        if password[i].isupper():
            upperCase += 1
            
        if password[i].islower():
            lowerCase += 1
            
        i = i + 1
    
    if numberCount == 0:
        print("no digits")
    
    if upperCase == 0:
        print("no upper case")
        
    if lowerCase == 0:
        print("no lower case")
        
    return
# Task 5 Finish

# Task 10 Start
def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    
    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0
    
    for char in txt:
        if char.isupper():
            uppr += 1
        elif char.islower():
            lowr += 1
        elif char.isdigit():
            dgts += 1
        elif char.isspace():
            whtspc += 1
    
    return uppr, lowr, dgts, whtspc
# Task 10 Finish
