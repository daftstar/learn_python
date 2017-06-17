# Example: Simple iteration - reduction of multiplication function.
# recursion creates scope within scope


def mult_iter(a, b):
    """ instead of a * b, repeat a + a, b times """
    result = 0
    while b > 0:
        result += a
        b -= 1
    return (result)


print (mult_iter(2, 5))
print ()

# Recursive factorial

def fact(n):
    if n == 1:
        return 1
    else:
        factorial = (n * fact(n-1))
        print (factorial)
        return (factorial)
        # once fact(n-1) == 1, then the function returns


print (fact(5))

# COMPARISON


# iteration
def factorial_iter(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return (prod)


# recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n - 1))

