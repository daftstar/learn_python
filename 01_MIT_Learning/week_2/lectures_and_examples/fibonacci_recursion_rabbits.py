def fib_rabbit(months):
    """
    How many pairs of rabbits will exist after x months?

    assumes months = int >= 0
    returns Fibonacci of x

    rabbits can only create other rabbits after 1 month
    rabbits have a 1 month gestational period
    thus new rabbits are born 2 months after original rabbits born
    """

    if months == 0 or months == 1:
        return 1
    else:
        return fib_rabbit(months-1) + fib_rabbit(months-2)

print (fib_rabbit(5))
