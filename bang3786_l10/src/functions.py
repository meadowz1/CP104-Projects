"""
------------------------------------------------------------------------
Lab 10 Functions
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = "2020-04-20"
------------------------------------------------------------------------
"""

# Tasks 1, 5, 6, 10, 13


# Task 1 Start
def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    result = list()
    
    first_result = fh.readlines()
    
    if (n) < len(first_result): 
        result = first_result[n].strip().split(',')
        
    return result
# Task 1 End


# Task 4 Start
def customer_first(fh):
    """
    -------------------------------------------------------
    Find the customer with the earliest sign-up date.
    Assumes file is not empty.
    Use: result = customer_first(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the earliest sign-in date (list)
    -------------------------------------------------------
    """
    line = fh.readline()

    earliest_date = None
    earliest_customer = None

    while line:
        fields = line.strip().split(',')

        sign_up_date = fields[-1]

        if earliest_date is None or sign_up_date < earliest_date:
            earliest_date = sign_up_date
            earliest_customer = fields

        line = fh.readline()

    return earliest_customer
# Task 4 End


# Task 5 Start
def customer_append(fh, fields):
    """
    -------------------------------------------------------
    Appends a customer record to a comma-delimited sequential file.
    Use: customer_append(fh, fields)
    -------------------------------------------------------
    Parameters:
        fh - file to add to (file handle - already open for appending)
        fields - a list of the field data to append to the file (list)
    Returns:
       None
    -------------------------------------------------------
    """
    newfield = ",".join(str(field) for field in fields)
    
    fh.write(newfield + "\n")
    
    print("data appended to file")
    
    return
# Task 5 End


# Task 6 Start
def number_stats(fh):
    """
    -------------------------------------------------------
    Returns statistics on the numbers in a file.
    Assumes file is not empty.
    Use: smallest, largest, total, average = number_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        smallest - smallest number (int)
        largest - largest number (int)
        total - sum of all the numbers in the file (int)
        average - average of all the numbers (float)
    ------------------------------------------------------
    """
    line = fh.readline()

    smallest = largest = int(line.strip())
    

    total = smallest
    
    count = 1 
    
    line = fh.readline()
    
    while line != "":
        num = int(line.strip())

        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

        total += num
        
        count += 1
        
        line = fh.readline()

    average = total / count
    
    return smallest, largest, total, average
# Task 6 End
 
    
# Task 10 Start
def count_frequency_word(fh, word):
    """
    -------------------------------------------------------
    Counts the number of appearances of word in fh.
    Case is significant - line in file must match word in case.
    Use: count = count_frequency_word(fh, word)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        word - the word to search for it in fh (str)
    Returns:
        count - the number of appearance of word in fh (int)
    ------------------------------------------------------
    """
    count = 0

    for line in fh:
        words = line.split()

        count += words.count(word)
    
    return count
# Task 10 End


# Task 13 Start
def file_copy(fh_1, fh_2):
    """
    -------------------------------------------------------
    Copies the contents of fh_1 to fh_2.
    Any contents of fh_2 are overwritten.
    Use: file_copy(fh_1, fh_2)
    -------------------------------------------------------
    Parameters:
        fh_1 - source file (file handle - already open for reading)
        fh_2 - target file (file handle - already open for writing)
    Returns:
        None
    ------------------------------------------------------
    """
    
    source = fh_1.read()

    fh_2.seek(0)

    fh_2.write(source)

    fh_2.truncate()
    
    return
# Task 13 End

