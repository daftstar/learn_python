def largest_odd_times(L):
    """
    Assumes L is a non-empty list of ints
    Returns the largest element of L that occurs an odd number
    of times in L. If no such element exists, returns None
    """
    # init dictionaries for all counts and odd counts
    all_int_count = {}
    odd_int_count = {}

    # populate instances of each list value to dict all_int_count
    for number in L:
        if number in all_int_count:
            all_int_count[number] += 1
        else:
            all_int_count[number] = 1

    # populate all odd value instances from all_int_count to
    # dict odd_int_count
    for key, value in all_int_count.items():
        if value % 2 != 0:
            odd_int_count[key] = value

    # if the odd_int_count dict is empty, then return 0
    # otherwise, return the largest key value
    if len(odd_int_count) == 0:
        max_value = None
    else:
        max_value = max(odd_int_count)

    return max_value


# L = [3, 3, 3, 5, 5, 9, 19, 19, 19, 21]
# L = [2,2,4,4]
L = [3, 3, 3, 5, 5, 9, 19, 19, -19, -21, -21, 9, 9, 9, 9]

print ()
print (largest_odd_times(L))
