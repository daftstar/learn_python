# PROBLEM 4
# Write a function is_triangular that meets the
# specification below.

"""
A triangular number is a number obtained by the continued
summation of integers starting from 1.

For example, 1, 1+2, 1+2+3, 1+2+3+4, etc.,
corresponding to 1, 3, 6, 10, etc., are triangular numbers.
"""


def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    if k == 1:
        return True

    # create a list to check values against.
    # for consistent lookups, create a dictionary
    check = []

    # initialize triangle for calculation
    triangle = 0

    # create a list of triangular numbers from 0, to k
    # Clean this up later since initial values in [check]
    # can hog up memory when k is very large.
    for i in range(0, k):
        triangle += i
        check.append(triangle)

        # no need to continue calculating triangular numbers if the
        # latest number in the list is greater than what we're
        # checking for.
        if check[-1] > k:
            break

    # for debugging / visualization purposes:
    # print (check)
    # print (check[-3:])

    # check if k is within the last 3 values of
    # generated triangular values. No need to check if
    # k is in the earlier values since k will be > than
    # those values.
    return (k in (check[-3:]))


print (is_triangular(994755))






# ORIGINAL FUNCTION:
# PROBLEM 4
# Write a function is_triangular that meets the
# specification below.

# """
# A triangular number is a number obtained by the continued
# summation of integers starting from 1.

# For example, 1, 1+2, 1+2+3, 1+2+3+4, etc.,
# corresponding to 1, 3, 6, 10, etc., are triangular numbers.
# """


# def is_triangular(k):
#     """
#     k, a positive integer
#     returns True if k is triangular and False if not
#     """
#     if k == 1:
#         return True

#     # create a list to check values against.
#     # for consistent lookups, create a dictionary
#     check = []

#     # initialize triangle for calculation
#     triangle = 0

#     # create a list of triangular numbers from 0, to k
#     for i in range(0, k):
#         triangle += i
#         check.append(triangle)

#         # no need to continue calculating triangular numbers if the
#         # latest number in the list is greater than what we're
#         # checking for.
#         if check[-1] > k:
#             break

#     # for debugging / visualization purposes:
#     print (check)
#     # check if k is in the list of generated triangular values.
#     # print (check in range[])
#     if k in check:
#         return True
#     else:
#         return False


# print (is_triangular(1891))

