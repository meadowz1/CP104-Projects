"""
------------------------------------------------------------------------
Lab 11, Functions
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-12-01'
------------------------------------------------------------------------
"""

import random

# Task 1 Start
def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    
    # Creating a blank matrix for appending lists to
    matrix = []
    
    # Using a for loop inside a for loop to make rows and columns
    for i in range(rows):
        row = []
        
        for j in range(cols):
            # Checking if the value_type is 'float', 'int', or something else
            # If the value is something else, the value returned is always 0.
            if value_type == 'float':
                value = random.uniform(low, high)
                
            elif value_type == 'int':
                value = random.randint(low, high)
                
            else:
                value = 0
            
        # Appending the values to rows, then appending the whole row to the matrix
            row.append(value)
            
        matrix.append(row)
        
    return matrix
# Task 1 End

# Task 2 Start
def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    # Blank list for holding lists from the loop
    matrix = []
    
    # for loop inside a for loop to append lists to the matrix list
    for i in range(rows):
        row = []
        for j in range(cols):
            # random.choice() allows the code to select a part of a string randomly
            value = random.choice('abcdefghijklmnopqrstuvwxyz')
            
            # appending the values to the row list, then appending the row lists to the matrix
            row.append(value)
        
        matrix.append(row)
    
    return matrix
# Task 2 End

# Task 3 Start
def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    
    # Checks if the matrix has values or not, using
    # an if statement makes this skip to the end if 
    # the matrix is empty.
    if not matrix: 
        print("No values")
    
    # Continues the program if the matrix does have values.
    else:
        # Printing the headers
        print(f"{' ':>3}", end = "")
        for col in range(len(matrix[0])):
            print(f"{col + 0:5}", end = "")
        print()    
        
        # Printing the rows
        for row_index, row in enumerate(matrix):
            print(f"{row_index + 0:2} ", end = "")
            
            # Printing the values
            for value in row:
                if value_type == 'float':
                    print(f"{value:5.2f}", end="")
                    
                elif value_type == 'int':
                    print(f"{value:5d}", end="")
                    
                else: 
                    print(f"{0:5d}", end="")
            
            # Blank print for formatting       
            print()
    
    return 
# Task 3 End

# Task 4 Start
def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """
    # FYI: I Salvaged most of the code from task 3
    #      as they align very well and work together.
    
    # Checks if the matrix has values or not, using
    # an if statement makes this skip to the end if 
    # the matrix is empty.
    if not matrix: 
        print("No values")
    
    # Continues the program if the matrix does have values.
    else:
        # Printing the headers
        print(f"{' ':>3}", end = "")
        for col in range(len(matrix[0])):
            print(f"{col + 0:5}", end = "")
        print()    
        
        # Printing the rows
        for row_index, row in enumerate(matrix):
            print(f"{row_index + 0:2} ", end = "")
            for value in row:
                print(f"{value:>5s}", end="")
            
            # Blank print for formatting
            print()
    
    return
# Task 4 End

# Task 5 Start
def words_to_matrix(word_list):
    """
    -------------------------------------------------------
    Generates a 2D list of character values from the given
    list of words. All words must be the same length.
    Use: matrix = words_to_matrix(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a list containing the words to be placed in
            the matrix (list of string)
    Returns:
        matrix - a 2D list of characters of the given words
         in word_list (2D list of string).
    -------------------------------------------------------
    """
    # Blank matrix
    matrix = []
    
    # Checking to see if list is empty
    if not word_list:
        matrix = ["no"]
    
    else:
        # Splits up each word in the list.
        for word in word_list:
            character = []
            
            for char in word:
                character.append(char)
                
            matrix.append(character)
    
    return matrix 
# Task 5 End

# Task 6 Start
def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    # Sets smallest, largest, and total variables
    smallest = float('inf')
    largest = float('-inf')
    total = 0
    
    if not matrix:
        smallest = 0
        largest = 0 
        total = 0
        average = 0
    
    else:
        # Looks for each number inside the lists inside the matrix
        for row in matrix:
            for num in row:
                if num < smallest:
                    smallest = num
                    
                if num > largest:
                    largest = num
                
                total += num
        
        # Counts how many items are in the matrix by multiplying the length of the matrix 
        # by the length of the first list in the matrix
        count = len(matrix) * len(matrix[0])
        
        average = total / count
    
    return smallest, largest, total, average
# Task 6 End
    
# Task 7 Start
def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """
    # Getting values and setting values to make traversing the matrix
    # simpler and quicker.
    
    if not matrix:
        min_loc = [0, 0]
        max_loc = [0, 0]
    
    else:
        rows = len(matrix)
        cols = len(matrix[0])
        min_val = matrix[0][0]
        max_val = matrix[0][0]
        min_loc = [0, 0]
        max_loc = [0, 0]
        
        # Using for loops to look at each individual value
        for i in range(rows):
            for j in range(cols):
                
                # finding if the value is smaller
                if matrix[i][j] < min_val:
                    min_val = matrix[i][j]
                    min_loc = [i, j]
                
                # finding if the value is larger
                elif matrix[i][j] > max_val:
                    max_val = matrix[i][j]
                    max_loc = [i, j]
    
    return min_loc, max_loc
# Task 7 End

# Task 8 Start
def find_less(matrix, n):
    """
    -------------------------------------------------------
    Finds the location [row, column] of the first value in matrix
    that is smaller than a target value, n. If there is no such
    number in matrix, it should return an empty list.
    Use: loc = find_less(matrix, n)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
        n - the target value (float)
    Returns:
        loc - a list of the row and column location of
            the first value smaller than n in values,
            an empty list otherwise (list of int)
    -------------------------------------------------------
    """
    if not matrix:
        loc = []
    
    else:
        # Getters and Setter for matrix values
        rows = len(matrix)
        cols = len(matrix[0])
        loc = [] 
        
        # Simple for loop to traverse the matrix
        for i in range(rows):
            for j in range(cols):
                # Using a break since we only want the first value that
                # is smaller than the n value
                if matrix[i][j] < n:
                    loc = [i,j]
                    break
    
    return loc
# Task 8 Finish

# Task 9 Start
def count_frequency(matrix, char):
    """
    -------------------------------------------------------
    Count the number of appearances of the given character char
    in matrix.
    Use: count = count_frequency(matrix, char)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to search in it (2D list of str)
        char - character to search for it (str, len = 1)
    Returns:
        count - the number of appearances of char in the matrix (int)
    -------------------------------------------------------
    """
    if not matrix:
        count = 0
    
    else:
        # Getters and setters for matrix values and counting
        count = 0
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Simple For Loop to traverse the matrix
        for i in range(rows):
            for j in range(cols):
                # Checking if the character in the spot [i, j] == char
                if matrix[i][j] == char:
                    count += 1
    
    return count
# Task 9 Finish

# Task 10 Start
def find_word_horizontal(matrix, word):
    """
    -------------------------------------------------------
    Look for word in each row of the given matrix of characters.
    Returns a list of indexes of all rows that are equal to word.
    Returns an empty list if no row is equal to word.
    Use: rows = find_word_horizontal(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix of characters (2D list of str)
        word - the word to search for (str)
    Returns:
        rows - a list of row indexes (list of int)
    ------------------------------------------------------
    """
    if not matrix:
        rows = []
    
    else:
        # Simple getters and setters for counting and traversing
        row = len(matrix) # just for length of the matrix
        rows = [] # storing the index of words found
        
        for i in range(row):
            # Using the .join function to make the split up characters
            # into one word for checking
            row_word = ''.join(matrix[i])
            
            if row_word == word:
                rows.append(i)
        
    return rows
# Task 10 Finish

# Task 11 Start
def find_word_vertical(matrix, word):
    """
    -------------------------------------------------------
    Look for word in each column of the given matrix of characters.
    Returns a list of indexes of all column that are equal to word.
    Returns an empty list if no column is equal to word.
    Use: cols = find_word_vertical(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix of characters (2D list of str)
        word - the word to search for (str)
    Returns:
        cols - a list of column indexes (list of int)
    ------------------------------------------------------
    """
    if not matrix:
        cols = []
    
    else:
        # Simple getters and setters for counting and traversing
        row = len(matrix) # length of matrix
        col = len(matrix[0]) # length of lists in matrix
        cols = [] # index of found values
        
        for j in range(col):
            # Convert the column to a string and check if it equals word
            col_str = ''.join(matrix[i][j] for i in range(row))
            if col_str == word:
                cols.append(j)
                
    return cols           
# Task 11 End

# Task 12 Start
def find_word_diagonal(matrix, word):
    """
    -------------------------------------------------------
    Returns whether word is on the diagonal of a square matrix
    of characters.
    Use: found = find_word_diagonal(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - a 2d list of characters (2d list of str)
        word - the word to compare against the diagonal of matrix (str)
    Returns:
        found - True if word is on the diagonal of matrix,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    if not matrix:
        found = False
        
    else:
        length = len(matrix)
        found = False
        
        diagonal = ''.join(matrix[i][i] for i in range(length))
        
        if diagonal == word:
            found = True
    
    return found
# Task 12 End

# Task 13 Start 
def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    if not matrix:
        num = num
    
    else:
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = matrix[i][j] * num
        
    return
# Task 13 Finish

# Task 14 Start
def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """
    if not matrix:
        transposed = []
    
    else:
        rows = len(matrix)
        cols = len(matrix[0])
        transposed = [[None] * rows for k in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = matrix[i][j]
        
    return transposed
# Task 14 Finish

# Task 15 Start
def matrix_equal(matrix1, matrix2):
    """
    -------------------------------------------------------
    Compares two matrices to see if they are equal - i.e. have the
    same contents in the same locations.
    Use: equal = matrix_equal(matrix1, matrix2)
    -------------------------------------------------------
    Parameters:
        matrix1 - the first matrix (2D list of *)
        matrix2 - the second matrix (2D list of *)
    Returns:
        equal - True if matrix1 and matrix2 are equal,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    if not matrix1:
        equal = False
    
    elif not matrix2:
        equal = False
    
    else: 
        rows1 = len(matrix1)
        rows2 = len(matrix2)
        cols1 = len(matrix1[0])
        cols2 = len(matrix2[0])
        equal = True
        
        if rows1 != rows2:
            equal = False
        
        elif cols1 != cols2:
            equal = False
            
        else:
            for j in range(rows1):
                for k in range(cols1):
                    if matrix1[j][k] == matrix2[j][k]:
                        equal = True
                    else:
                        equal = False
                    
    return equal
# Task 15 Finish