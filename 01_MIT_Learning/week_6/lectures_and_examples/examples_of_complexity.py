# LOGARITHMIC COMPLEXITY O(log n)


def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'

    result = ''
    while i > 0:
        result = digits[i % 10] + result
        # result += digits[i % 10] - this reverses the order
        i = i//10
        print (result, i)
    return result


print (intToStr(987650))
# question is how many times do we have to divide by 10?
# linear in the digits of n, but log in the size of n.


# --------------------------------------------------------------
# LINEAR COMPLEXITY O(n)
def addDigits(s):
    val = 0
    for c in s:
        val += int(c)
    return val


print (addDigits("123493"))


def fact_iter(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


print (fact_iter(1))


# the recursive function is still O(n) because function calls
# are linear to n. Recursive may take more time, but number
# steps called is fewer.

def fact_recur(n):
    """ assume n > 0 """
    if n < 1:
        return 1
    else:
        return n * (fact_recur(n-1))


print (fact_recur(3))


# --------------------------------------------------------------
# Exponential Complexity O(c^n)

def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]]     # list of empty files
    smaller = genSubsets(L[:-1])    # all subsets without last element
    extra = L[-1:]      # create list of just last element
    new = []
    for small in smaller:
        new.append(small+extra) # for all smaller solutions, add one with last element
    return smaller + new    # combine those with last element and those without

L = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
# L = [1, 2]
hey = genSubsets(L)
print (len(hey))





"""O(log(n)) - Logarithmic"""
#   log n + 1000

""" O(n) - Linear"""
#   5n
#   10log(n) + 5n


"""O(n^c) - Polynomial"""
#   3n^2 + 2n - 100
#   10log(n) + 5n^2
#   3n^3 - 2000 n^2
#   2n^2

""" O(n log(n))- LogLinear """
#   50n + nlog(n)

"""O(c^n - Exponential)"""
#   2^n + n^2





