#!/usr/bin/env python3

# For completion of Homework 04 at pirple.com
# Walter Spicer

"""
Create a global variable called myUniqueList. It should be an empty list to start.

Next, create a function that allows you to add things to that list. Anything that's passed to this function should get added to myUniqueList, unless its value already exists in myUniqueList. If the value doesn't exist already, it should be added and the function should return True. If the value does exist, it should not be added, and the function should return False;

Finally, add some code below your function that tests it out. It should add a few different elements, showcasing the different scenarios, and then finally it should print the value of myUniqueList to show that it worked.

Extra Credit:

Add another function that pushes all the rejected inputs into a separate global array called myLeftovers. If someone tries to add a value to myUniqueList but it's rejected (for non-uniqueness), it should get added to myLeftovers instead.
"""

# using PEP-8 naming convention of snake_case
# thus myUniqueList is renamed my_unique_list
# also myLeftovers is renamed my_leftover_list to be consistent and more descriptive

# only learned [:] and append() in lesson
# found elsewhere that the keyword 'in' would tell me if an element exists in the List
# can also use negation 'not in'

my_unique_list = []
my_leftovers_list = []


def add_to_list(value):
    """
        If value not found in my_unique_list, it will append it.
        Otherwise duplicates are sent to the add_to_leftovers() function.
    """
    if value not in my_unique_list:
        my_unique_list.append(value)
        return True
    else:
        add_to_leftovers(value)
        return False


def add_to_leftovers(value):
    """
        Append values to the my_leftovers_list
    """
    my_leftovers_list.append(value)


print(my_unique_list)
print(my_leftovers_list)

print("The question I ask myself: {}".format(
    add_to_list('why does the instructor use title CamelCase?')))
print("Another question: {}".format(
    add_to_list('I wonder if I missed the in and not in keywords?')))

print(f"Adding 42 to list returns: {add_to_list(42)}")
print(f"Adding 42 to the list again returns: {add_to_list(42)}")

print(
    f"Adding another List to the list returns: {add_to_list(['Hello', 55, False])}")

print(f"Contents of my_unique_list: {my_unique_list}")
print(f"Contents of my_leftovers_list: {my_leftovers_list}")
