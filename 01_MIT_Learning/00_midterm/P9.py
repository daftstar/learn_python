"""
Write a Python function that takes in two lists and
calculates whether they are permutations of each other.

The lists can contain both integers and strings.
We define a permutation as follows:

    - the lists have the same number of elements
    - list elements appear the same number of times in both lists

If the lists are not permutations of each other,
the function returns False. If they are permutations of each other,
the function returns a tuple consisting of the following elements:

    - the element occuring the most times
    - how many times that element occurs
    - the type of the element that occurs the most times

If both lists are empty return the tuple (None, None, None).
If more than one element occurs the most number of times,
you can return any of them.

For example,
if L1 = ['a', 'a', 'b'] and L2 = ['a', 'b']
then is_list_permutation returns False

 if L1 = [1, 'b', 1, 'c', 'c', 1]
and L2 = ['c', 1, 'b', 1, 1, 'c']
then is_list_permutation returns
(1, 3, <class 'int'>) because the integer 1 occurs the most,
3 times, and the type of 1 is an integer
(note that the third element in the tuple is not a string).
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
    If they are permutations of each other,
    returns a tuple of 3 items in this order:
        the element occurring most, how many times it occurs,
        and its type
    '''
    L1_count = {}
    L2_count = {}
    max_count = 0
    max_key = None

    # If we were given empty lists, return None tuple triplet
    if len(L1) == 0 and len(L2) == 0:
        return (None, None, None)

    # Create key, value count dictionaries for L1 and L2
    for i in L1:
        if i in L1_count:
            L1_count[i] += 1
        else:
            L1_count[i] = 1

    for i in L2:
        if i in L2_count:
            L2_count[i] += 1
        else:
            L2_count[i] = 1

    # Conditional logic for what happens if L1 == L2
    if L1_count == L2_count:
        # get the max value count within L1 (assumes L1 == L2)
        max_count = max(L1_count.values())

        # find which key has the value of max_count, assign to max_key
        for key, value in L1_count.items():
            if value == max_count:
                max_key = key

        # return tuple, per instruction
        return (max_key, max_count, type(max_key))

    # if L1 != L2, then return False
    else:
        return False



# L1 = []
# L2 = []

# L1 = ["hello", 1, 1, 1, 'b', 'c', 'c']  # {'b': 1, 1: 3, 'c': 2, 'hello': 1}
# L2 = [1, 1, 1, 'c', 'c', 'b', "hello"]

# L1 = ["hello", 1, 1, 1, 'b', 'c', 'c']
# L2 = [1, 1, 1, 'c', 'c', 'b', "heddllo"]

L1 = [1, 1, 1, 'b', 'c', 'c']
L2 = [1, 1, 1, 'c', 'c', 'b']

# L1 = [1, 1, 1, 'b', 'c', 'c', "hey", "hey", "hey", "hey"]
# L2 = ["hey", "hey", "hey", "hey", 1, 1, 1, 'c', 'c', 'b']

# L1 = ['a', 'a', 'b']
# L2 = ['a', 'b']

print (is_list_permutation(L1, L2))
