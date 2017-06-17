
def square(x):
    return (x ** 2)


def fourth_power(x):
    '''
    x: int or float
    '''
    return (square(x) ** square(x))

print (fourth_power(2))



def odd(x):
    '''
    x: int
    returns: True if x is odd, False otherwise
    don't use an if statement
    '''

    return (x % 2 != 0)

print (odd(3))