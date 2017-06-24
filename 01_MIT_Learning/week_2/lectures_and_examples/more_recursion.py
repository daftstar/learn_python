def factI(n):
    """
    Assumes n an int > 0
    Returns n!
    """
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result

print (factI(5))


def factR(n):
    """
    Assumes n an int > 0
    returns n!
    """
    if n == 1:
        return n
    else:
        return n * factR(n-1)

print (factR(4))


# _________________________________________________________

def fib(x):
    global numFibCAlls
    numFibCAlls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def testFib(n):
    for i in range (n+1):
        global numFibCAlls
        numFibCAlls = 0
        print ("fib of %s: %s" % (i, fib(i)))
        print ("fib called %s times" % numFibCAlls)

print (testFib(6))