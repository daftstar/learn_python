# error handling allows you to provide users useful error messages

def new_line():
    print ("\n__________________________________\n")


def sqrt(x):
    """ return square root of value x """
    return x ** 0.5


print (sqrt(4))
print (sqrt(10))
new_line()


# print (sqrt("eheh"))
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'


# ####################################################
# Using Error Handling
#
# Errors & Exceptions
# Exception = caught during execution
# Catch exceptions with try-except clause
#   Runs code following try
#   If there's an exception, run the code following except
# ####################################################


def sqrt(x):
    """ returns the square-root of a number """
    try:
        return x ** 0.5
    except:
        print ("x MUST be an int or float")


print (sqrt(99))
sqrt("eheh")
new_line()


# ####################################################
# Using TypeError
# allows other errors to pass through
# ????
# ####################################################


def sqrt(x):
    """ returns the square-root of a number """
    try:
        return x ** 0.5
    except TypeError:
        print ("x MUST beeee an int or float")


print (sqrt(179))
sqrt([33, 331])
new_line()


# ##########################################################
# Using Raise to inform of errors if conditional is met
# While the function would still work, in this case
# we would want to prevent the function from moving forward
# ##########################################################


def sqrt_error_test(x):
    """ return square root of a number """
    if x < 0:
        raise ValueError('x must be non-negative')
    try:
        return (x ** 0.5)
    except TypeError:
        print ("x must be an int or a float")


print ("using 3:", sqrt_error_test(3))
print ("using negative:", sqrt_error_test(-3))   #ValueError: x must be non-negative


