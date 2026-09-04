# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# Name: Tess Vithoulkas

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
XXX Write your pseudocode here XXX

set value1 equal to 0
set value2 to 1
set counter equal to 1
set sum to 0

get input integer n

while counter variable is less than or equal to integer n
    set sum equal to sum plus value1
    set value3 equal to value1 plus value2
    set value1 equal to value2
    set value2 equal to value3
    counter increases by 1
return sum

    

"""

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6 # user input- this is the number of times the loop should iterate

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # keeps track of the number of times the loop has iterated through
total = 0 # variable to hold the sum of the fibonacci numbers

while count < N: # iterates while the count is less than the value the user input
    total = total + a # sum of the fibonacci numbers becomes the original sum plus the first fibonacci number-this had to be changed from b to a

    next_value = a + b # the next fibonacci number value is the sum of the original two
    a = b # the lower fibonacci number gets the value of the higher one
    b = next_value # the higher fibonacci number gets the value of the next fibonacci number

    count = count + 1 # count increases since loop has been iterated through

print(total) # sum is printed once the count is greater than the user input value

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.

import numpy
print(numpy.std([0,1,1,2,3,5,8,13,21,34]))

# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.

fibSeqList = []

def fibonacciSequence(n):
    value1 = 0
    value2 = 1
    counter = 1
    sum = 0

    while(counter <= n):
        sum += value1
        value3 = value1 + value2
        value1 = value2
        value2 = value3
        counter += 1
    fibSeqList.append(sum)

fibonacciSequence(5)
fibonacciSequence(10)
fibonacciSequence(15)
fibonacciSequence(20)
fibonacciSequence(25)
fibonacciSequence(30)

print(fibSeqList)

# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0 #changed this value from a string to an int to fix the error and make output correct
    b = 1 #changed this value from a string to an int to fix the error and make output correct
    index = 0 #had to add this definition outside the while loop so the variable could be returned outside the loop (set equal to 0 since the index of the first number in a list when coding is 0)

    while a <= limit: #TypeError: Python can't compare strings and integers to see if they are equal (<= not supported between str and int)- make the strings (a and b) an int to solve this problem and make the output correct
        next_value = a + b
        a = b
        b = next_value
        index += 1

    return index #UnboundLocalError: Python can't access index variable since it was defined inside the while loop and we are calling it outside the loop- initiate variable outside loop to fix this


result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_even_fib(limit):
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 == 0:  # This line checks if the Fibonacci number is even
            total = b
        a, b = b, a + b
    return total


# Add your test cases here
sum_even_fib(2)
# %%
