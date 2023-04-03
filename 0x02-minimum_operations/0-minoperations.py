#!/usr/bin/python3

"""
    This is a function/method that calculates the least amount of operations 
    that is required in order to result in `n` `H` characters in a file. 
    It takes `n` as an argument which signifies 
    the number of characters to be displayed
"""

def minOperations(n):
    """This is a function/method that calculates the least amount of operations 
        that is required in order to result in `n` `H` characters in a file. 
        It takes `n` as an argument which signifies 
        the number of characters to be displayed
        return:
            number of minimum operations. Returns 0 if is not feasible"""
            
    number_of_operations = 0
    min_number_of_operations = 2
    
    if n < 2:
    # If n is less than 2, return 0 as it is not possible to obtain less than two 'H's.
        return 0
    
    # Divide n by the minimum operations until it is no longer divisible by the minimum operations.
    # Increment the minimum operations by 1 and repeat the process until n is reduced to 1.
    while n > 1: 
        # while there is at least one character left

        while n % min_number_of_operations == 0:
            #while we can still perform the minimum number of operations on the remaining characters without leaving any character untouched

            number_of_operations += min_number_of_operations
            # then we increase the number of operations since we can still carry out minimum operations and even more

            n /= min_number_of_operations
            # we reduce n to make sure that we can still carry out the minimum number of operations on it

        min_number_of_operations += 1
        #minimum number of operationsis increase. Eg, if we could copy and paste before, now we can copy, paste and copy again
    
    return number_of_operations
    # we finally return the numbner of operations that we were able to perform
