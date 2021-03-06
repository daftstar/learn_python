
# Python Constraints
# ======

# Your code will run inside a Python 2.7.6 sandbox.

# Standard libraries are supported except for:
# bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal,
# termios, thread, time, unicodedata, zipimport, zlib.

# ########################################
# Prison Labor Dodgers
# ########################################

# Commander Lambda is all about efficiency,
# including using her bunny prisoners for manual labor.
# But no one's been properly monitoring the labor shifts
# for a while, and they've gotten quite mixed up.

# You've been given the task of fixing them, but after you wrote
# up new shifts, you realized that some prisoners had been
# transferred to a different block and aren't available for their
# assigned shifts.

# And manually sorting through each shift list to compare against
# prisoner block lists will take forever -
# remember, Commander Lambda loves efficiency!

# Given two almost identical lists of prisoner IDs x and y
# where one of the lists contains an additional ID,
# write a function answer(x, y) that compares the lists and
# returns the additional ID.

# For example, given the lists
# x = [13, 5, 6, 2, 5]
# y = [5, 2, 5, 13]
# the function answer(x, y) would return 6 because
# the list x contains the integer 6 and the list y doesn't.

# Given the lists
# x = [14, 27, 1, 4, 2, 50, 3, 1]
# y = [2, 4, -4, 3, 1, 1, 14, 27, 50],
# the function answer(x, y) would return -4 because the list y
# contains the integer -4 and the list x doesn't.

# In each test case, the lists x and y will always contain n non-unique
# integers where n is at least 1 but never more than 99,
# and one of the lists will contain an additional unique integer
# which should be returned by the function.
# The same n non-unique integers will be present on both lists,
# but they might appear in a different order, like in the examples
# above. Commander Lambda likes to keep her numbers short,
# so every prisoner ID will be between -1000 and 1000.

# ##################################################
# OPTIMIZED WAY - PROOF OF CONCEPT
# Runs in 40 steps
# http://www.pythontutor.com/live.html#mode=edit
# ##################################################
x = [14, 27, 1, 4, 2, 50, 3, 1]
y = [2, 4, -4, 3, 1, 1, 14, 27, 50]


def answer(x, y):
    """ compares values of x against y
    and vice versa to find the unique value """
    # this solution only works for the last unique value found
    # use list comprehension to store multiple unique values

    # create a single list to look for unique values
    z = (x + y)

    # assumes that "unique" = 1 instance of a value
    for i in z:
        if z.count(i) % 2 != 0:
            new_value = i

    return (new_value)

print (answer(x, y))


# ##################################################
# ORIGINAL WAY - PROOF OF CONCEPT
# Runs in 163 steps
# http://www.pythontutor.com/live.html#mode=edit
# ##################################################

# def answer(x, y):
#     """ compares values of x against y
#     and vice versa to find the unique value """
#     for i in y:
#         if i not in x:
#             abnormal_value = i
#         else:
#             for i in x:
#                 if i not in y:
#                     abnormal_value = i

#     return (abnormal_value)






# Test cases
# ==========

# Inputs:
#     (int list) x = [13, 5, 6, 2, 5]
#     (int list) y = [5, 2, 5, 13]
# Output:
#     (int) 6

# Inputs:
#     (int list) x = [14, 27, 1, 4, 2, 50, 3, 1]
#     (int list) y = [2, 4, -4, 3, 1, 1, 14, 27, 50]
# Output:
#     (int) -4

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
