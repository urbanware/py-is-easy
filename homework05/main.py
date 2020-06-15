#!/usr/bin/env python3

# For completion of Homework 03 at pirple.com
# Walter Spicer

"""
Write a program that prints the numbers from 1 to 100.

But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".

For numbers which are multiples of both three and five print "FizzBuzz".

Plus extra bit for adding a test for Prime.
"""

fizzbuzz = []
fizz = []
buzz = []
prime = []

# PEP-8 default snake_case and style guide
# interesting needed the fizzbuzz check at the top otherwise it would exit the if too early
# also I needed a separate function for prime as they were doing two
# different things.
# format of function with is_blah for Boolean returns of True or False


def print_fizzbuzz(n):
    """
    Returns:
    FizzBuzz divisible by 3 and 5
    Fizz divisible by 3
    Buzz divisible by 5
    Prime test goes to another function
    """
    for num in range(1, n+1):
        if is_prime(num):
            print("Prime")
            prime.append(num)
        elif num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
            fizzbuzz.append(num)
        elif num % 5 == 0:
            print("Buzz")
            buzz.append(num)
        elif num % 3 == 0:
            print("Fizz")
            fizz.append(num)
        else:
            print(num)


def is_prime(num):
    """
    Return True if a prime number.  False if not a prime number.
    When called it is already plus 1 in calling loop
    otherwise would need to plus one the num so loop hits the value.
    Also needed two variables not one to work so that it tests the loop
    up to the value. 
    """

    if num == 1:
        return False
    # elif num % i == 0:
    #     return False
    # else:
    #     return True
    # #fail

    # Need both the interator and a value
    # modulo divide by iterator i
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Reminder to self that is_prime is num+1
# for n in range(1, 13):
#     if is_prime(n) == True:
#         print(n)


print_fizzbuzz(100)
print("*"*40)
print("Fizz:", fizz)
print("Buzz:", buzz)
print("FizzBuzz:", fizzbuzz)
print("Prime:", prime)
