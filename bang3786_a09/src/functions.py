"""
------------------------------------------------------------------------
Assignment 9 Functions
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-12-02'
------------------------------------------------------------------------
"""

# Task 1 Start
def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    while i != count:
        print(file_handle.readline(), end="")
        i += 1
    
    return
# Task 1 End


# Task 2 Start
def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    number_list = []

    line = file_handle.readline()
    
    while line != '':
        token = line.split(',')
        for i in range(len(token)):
            item = token[i]
            if item.strip().isdigit():
                number = int(item)
                if number > 0:
                    number_list.append(number)
        
        line = file_handle.readline()
        
    return number_list
# Task 2 End


# Task 3 Start
def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    ucount = lcount = dcount = wcount = rcount = 0

    file_content = file_handle.read()

    for char in file_content:
        if char.isupper():
            ucount += 1
        elif char.islower():
            lcount += 1
        elif char.isdigit():
            dcount += 1
        elif char.isspace():
            wcount += 1
        else:
            rcount += 1

    return ucount, lcount, dcount, wcount, rcount
# Task 3 End


# Task 4 Start
def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    content = fh_read.readlines()

    for i, line in enumerate(content):
        fh_write.write(f"[{i}] {line}")
    
    return
# Task 4 End


# Task 5 Start
def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    lowest_mark = float('inf')
    highest_mark = float('-inf')
    total_marks = 0
    count = 0
    l_id = 0
    h_id = 0
    avg = 0

    lines = file_handle.readlines()

    for line in lines:
        parts = line.strip().split(',')

        student_id = parts[2]
        mark = float(parts[3])

        total_marks += mark
        count += 1

        if mark < lowest_mark:
            lowest_mark = mark
            l_id = student_id

        if mark > highest_mark:
            highest_mark = mark
            h_id = student_id

    avg = total_marks / count if count > 0 else 0.0

    return l_id, h_id, avg
# Task 5 End