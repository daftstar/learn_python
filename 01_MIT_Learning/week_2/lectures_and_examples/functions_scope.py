def a(x):
    '''
    x: int or float.
    '''
    return x + 1


def b(x):
    '''
    x: int or float.
    '''
    return x + 1.0


def c(x, y):
    '''
    x: int or float.
    y: int or float.
    '''
    return x + y


def d(x, y):
    '''
    x: Can be of any type.
    y: Can be of any type.
    '''
    return x > y


def e(x, y, z):
    '''
    x: Can be of any type.
    y: Can be of any type.
    z: Can be of any type.
    '''
    return x >= y and x <= z


def f(x, y):
    '''
    x: int or float.
    y: int or float
    '''
    x + y - 2


print (a(6))                    # 7
print (a(-5.3))                 # -4.3
print (a(a(a(6))))              # 9
print (c(a(1), b(1)))           # 4.0
# print (d('apple', 11.1))      # invalid
print (e(a(3), b(4), c(3, 4)))  # False
print (f)                       # function
print ()                        #


# ___________________________________

def a(x, y, z):
    if x:
        return y
    else:
        return z


def b(q, r):
    return a(q > r, q, r)


print (a(False, 2, 3))          # 3
print (b(3, 2))                 # 3
print (a(3 > 2, a, b))          # function
# print (b(a, b))               # invalid


x = 12


def g(x):
    """ hey! this is docstring """
    x = x + 1

    def h(y):
        return (x + y)
    return (h(6))


print (g(x))
print ()

# ___________________________________


def foo(x, y=5):
    def bar(x):
            return x + 1
    return bar(y * 2)


# print (foo(3))


def foo(x, y=5):
    def bar(x):
            return x + 1
    return bar(y * 2)
          
print (foo(3, 0))

