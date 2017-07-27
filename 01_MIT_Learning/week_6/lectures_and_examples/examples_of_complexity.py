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


# print (intToStr(987650))
# question is how many times do we have to divide by 10?
# linear in the digits of n, but log in the size of n.


# --------------------------------------------------------------
# LINEAR COMPLEXITY O(n)
def addDigits(s):
    val = 0
    for c in s:
        val += int(c)
    return val


# print (addDigits("123493"))


def fact_iter(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


# print (fact_iter(1))


# the recursive function is still O(n) because function calls
# are linear to n. Recursive may take more time, but number
# steps called is fewer.

def fact_recur(n):
    """ assume n > 0 """
    if n < 1:
        return 1
    else:
        return n * (fact_recur(n-1))


# print (fact_recur(3))


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
# hey = genSubsets(L)
# print (len(hey))





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


def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

# L = [0, 1, 2, 3, 4, 5, 6, 77, 99, 132, 154, 178]
# L = [2, 3, 6]
# L = [5, 10, 15, 20, 40, 80, 99]
# L = [1, 2, 5]
L = [1, 5, 999999]

# print (search(L, 5))
# print (newsearch(L, 5))


def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)

L = [2200, 13, 2, 3, 4, 99, 6, 77]
# print (swapSort(L))
print ()



def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)

L = [14, 2200, 13, 2, 3, 4, 99, 6, 77]
L = [20083, 2200, 13, 2, 3, 4, 99, 6, 77, 10200202]
L = [1, 2, 3, 4, 5, 6]
L = [1, 7, 2, 4, 6, 5]
print (modSwapSort(L))

