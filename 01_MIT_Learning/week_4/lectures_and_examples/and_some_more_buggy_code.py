def f(n):
    """
    n: integer, n >= 0.
    OUTPUTS:
    """
    if n == 0:
        return 1
    else:
        return n * f(n-1)


print (f(3))    # GET 0, SHOULD GET 6
print (f(1))    # GET 0, SHOULD GET 1
print (f(0))    # GET 0, SHOULD GET 0
print ()


def f(n):
    """
    n: integer, n >= 0.
    OUTPUTS:
    """
    if n == 0:
        return n
    else:
        return n * f(n-1)


print (f(3))    # GET 0, SHOULD GET 6
print (f(1))    # GET 0, SHOULD GET 1
print (f(0))    # GET 0, SHOULD GET 0
