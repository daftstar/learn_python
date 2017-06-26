def fib_efficient(n, d):
    # d contains dictionary of base cases and return value
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]

    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        # this updates the dictionary of fibonacci values
        # this prevents recalculation of a known fib
        d[n] = ans
        # print (d)
        return ans


d = {1: 1, 2: 2}
numFibCalls = 0
print ("running efficient fibonacci...")
print (fib_efficient(10, d))
print ('function calls:', numFibCalls)
print ("\n______________________________\n")


#
# This fibonacci code is VERY inefficient
def fib_inefficient(n):
    global numFibCalls
    numFibCalls += 1

    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib_inefficient(n-1) + fib_inefficient(n-2)


numFibCalls = 0
print ("running INEFFICIENT fibonacci...")
print (fib_inefficient(10))
print ('function calls:', numFibCalls)
