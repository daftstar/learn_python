# ################################################################
#
# Write a function called dict_invert that takes in a dictionary
# with immutable values and returns the inverse of the dictionary.
# The inverse of a dictionary d is another dictionary
# whose keys are the unique dictionary values in d.

# The value for a key in the inverse dictionary is
# a sorted list (increasing order) of all keys in d that have
# the same value in d.

# For Example:

# d = {1:10, 2:20, 3:30}
#     dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
#
# d = {1:10, 2:20, 3:30, 4:30}
#     dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
#
# d = {4:True, 2:True, 0:True}
#     dict_invert(d) returns {True: [0, 2, 4]}
#
# ################################################################

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the
    instructions above
    '''
    # initialize inverse_dict, and sorted_inverse_dict
    inverse_dict = {}
    sorted_inverse_dict = {}

    # for each key and value in d,
    # see if the value exists as a key in inverse_dict.
    # if it does, then, append the key of d as a value into inverse_dict
    # if not, then create the inverted key, value pair
    for key, value in d.items():
        if value in inverse_dict:
            inverse_dict[value].append(key)
        else:
            inverse_dict[value] = [key]

    # sort the dictionary values in ascending order,
    # because leaving good enough alone isn't good enough =/
    for key, value in inverse_dict.items():
        sorted_inverse_dict[key] = sorted(value)

    return sorted_inverse_dict


# d = {1: 10, 2: 20, 3: 30}           # {10: [1], 20: [2], 30: [3]}
# d = {1: 10, 2: 20, 3: 30, 4: 30}    # {10: [1], 20: [2], 30: [3, 4]}
d = {4: True, 2: True, 0: True}     # {True: [0, 2, 4]}
# d = {8: 6, 2: 6, 4: 6, 6: 6}        # {6: [2, 4, 6, 8]}
# d = {0: 2, 9: 0, 2: 9, 5: 9}        # {0: [9], 9: [2, 5], 2: [0]}
# d = {2: 1, 3: 1}                    # {1: [2, 3]}

print (dict_invert(d))

#
# ORIGINAL FUNCTION (DID NOT SORT VALUES)
# 
# def dict_invert(d):
#     '''
#     d: dict
#     Returns an inverted dictionary according to the
#     instructions above
#     '''
#     # initialize inverse_dict
#     inverse_dict = {}

#     # for each key and value in d,
#     # see if the value exists as a key in inverse_dict.
#     # if it does, then, append the key of d as a value into inverse_dict
#     # if not, then create the inverted key, value pair
#     for key, value in d.items():
#         if value in inverse_dict:
#             inverse_dict[value].append(key)
#         else:
#             inverse_dict[value] = [key]

#     return inverse_dict