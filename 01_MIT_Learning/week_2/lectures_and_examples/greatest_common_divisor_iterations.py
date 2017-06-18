def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor
    of a & b.

    FOR EXAMPLE:
    gcd(2, 12) = 2
    gcd(6, 12) = 6
    gcd(9, 12) = 3
    gcd(17, 12) = 1

    a = 6
       1: O
    -> 2: O
       3: O
       4: X
       5: X
       6: O

    b = 4
       1: O
    -> 2: O 
       3: X
       4: O
"""

    '''

    # find smallest number between a and b
    test_val = min(a, b)

    # keep looping until test_val divides cleanly into a and b
    # start at the higest number and work backwards
    while (a % test_val != 0) or (b % test_val != 0):
        test_val -= 1

    return test_val

print (gcdIter(4205, 15))


# USING EUCLID'S algorithm:


def gcdRecur(a, b):
    if a == 0:
        return b
    else:
        # a = b % a     >> 5 % 3 = 2
        # b = a
        return gcdRecur(b % a, a)

print (gcdRecur(22,0))
