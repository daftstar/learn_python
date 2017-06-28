def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)


print (rem(2, 5))   # YES, Expected
print (rem(5, 5))   # YES, Expected
print (rem(9, 5))   # NONE, UNEXPECTED - 
print ()








# BUGGY CODE

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        rem(x-a, a)


print (rem(2, 5))   # YES, Expected
print (rem(5, 5))   # YES, Expected
print (rem(7, 5))   # NONE, UNEXPECTED problem is, it doesn't return anything
