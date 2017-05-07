
"""
# Scopes are searched:
# 1 - Local Scope
# 2 - Enclosing Functions
# 3 - Global
# 4 - Built-in
"""


def new_line():
    print("\n__________________________\n")


# ##################################################
# Nested functions
# ##################################################

def mod2plus5(x1, x2, x3):
    """ Returns the remainder plus 5 of three values """

    def inner(x):
        """ Returns the remainder, plus 5 of a single value """
        return ((x % 2) + 5)

    return (inner(x1), inner(x2), inner(x3))


print (mod2plus5(1, 2, 3))
new_line()


# ##################################################
# Returning functions / Closures
# ##################################################

def raise_val(n):
    """ Return the inner function """

    def inner(x):
        """ Raise x to the power of n. """
        raised = x ** n
        return (raised)

    return (inner)


square = raise_val(2)   # <function raise_val.<locals>.inner at 0x102869048>
""" square = function, where x ** n, n is defined as 2 """

cube = raise_val(3)     # <function raise_val.<locals>.inner at 0x1021690d0>
""" cube = function, where x ** n, n is defined as 3 """

print (square(2), cube(4))
new_line()


# ##################################################
# Nonlocal Definition
# ##################################################

def outer():
    """ prints the value of n """
    n = 1
    print ("Outer / Enclosing Scope value of n:", n)

    def inner():
        nonlocal n
        n = 2
        print ("Inner / Enclosed Scope value of n:", n)

    inner()
    print ("Final Outer / Enclosing Scope value of n:", n)


print (outer())
new_line()
