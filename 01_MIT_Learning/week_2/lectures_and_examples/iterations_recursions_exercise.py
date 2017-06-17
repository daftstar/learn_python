# Iteration Example


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    # use successive multiplication instead of powers
    # 3 ^ 4 = 3 * 3 * 3 * 3 = 81
    value = 1

    for i in range(1, exp + 1):
        value *= base
    return (value)


print (iterPower(3, 4))


# Recursion Example
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # use successive exponetials instead of iterations
    # 3 ^ 5 = 3 * 3 * 3 * 3 * 3
    # also  = 3^3 * 3*2 * 3^1

    if exp == 0:
        return 1

    elif exp == 1:
        return base
    else:
        return (base * recurPower(base, (exp - 1)))

print (recurPower(3, 5))