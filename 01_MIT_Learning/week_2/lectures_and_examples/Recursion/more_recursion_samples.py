# Factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print (factorial(5))



# Calculate sum of list of numbers
def list_sum(L):
    if len(L) == 1:
        return L[0]
    else:
        # print (L)
        return L[0] + list_sum(L[1:])


L = [1, 2, 3, 4, 5]
print (list_sum(L))


# Calculate Exponent
def exp(x, n):
    """
    Computes the result of x raised to the power of n.
        >>> exp(2, 3)
        8
        >>> exp(3, 2)
        9
    """

    if n == 0:
        return 1
    else:
        return x * exp(x, n-1)

print (exp(2, 4))
# exp(2, 4)
# +-- 2 * exp(2, 3)
# |       +-- 2 * exp(2, 2)
# |       |       +-- 2 * exp(2, 1)
# |       |       |       +-- 2 * exp(2, 0)
# |       |       |       |       +-- 1
# |       |       |       +-- 2 * 1
# |       |       |       +-- 2
# |       |       +-- 2 * 2
# |       |       +-- 4
# |       +-- 2 * 4
# |       +-- 8
# +-- 2 * 8
# +-- 16


# Flatten lists
def flatten_list(a, result=None):
    """
    Flattens a nested list.
        >>> flatten_list([ [1, 2, [3, 4] ], [5, 6], 7])
        [1, 2, 3, 4, 5, 6, 7]
    """
    if result is None:
        result = []

    for x in a:
        if isinstance(x, list):
            flatten_list(x, result)
        else:
            result.append(x)

    return result


print (flatten_list([[1, 2, [3, 4] ], [5, 6, 6], 6, 7]))
