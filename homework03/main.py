#!/usr/bin/env python3

# For completion of Homework 03 at pirple.com
# Walter Spicer

"""
Details:

Create a function that accepts 3 parameters and checks for equality between any two of them.

Your function should return True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others.


Extra Credit:

Modify your function so that strings can be compared to integers if they are equivalent. For example, if the following values are passed to your function:

6,5,"5"

You should modify it so that it returns true instead of false.

Hint: there's a built in Python function called "int" that will help you convert strings to Integers.
"""

# using PEP-8 function and variable naming conventions.
# playing around with .format() and f-strings to see how they manage variables in print

# 1 and 2
# 1 and 3
# 2 and 1 (repeat thus not used)
# 2 and 3
# 3 and 1 (repeat thus not used)
# 3 and 2
# thus four if conditions used.


def check_equality(option_one, option_two, option_three):

    option_one = int(option_one)
    option_two = int(option_two)
    option_three = int(option_three)

    is_equal = False

    if option_one == option_two:
        is_equal = True
        print("Options are {} {} {}.  First and Second option equivalency is {}".format(
            option_one, option_two, option_three, is_equal))
    elif option_one == option_three:
        is_equal = True
        print("Options are {} {} {}.  First and Third option equivalency is {}".format(
            option_one, option_two, option_three, is_equal))
    elif option_two == option_three:
        is_equal = True
        print(
            f"Options are {option_one} {option_two} {option_three}.  Second and Third option equivalency is {is_equal}")
    else:
        print(
            f"Options are {option_one} {option_two} {option_three}.  The equivalency is {is_equal}")


print("*" * 40)

check_equality(5, 5, "6")
check_equality(6, 5, "5")
check_equality(5, 6, "5")
check_equality(6, 5, "7")
