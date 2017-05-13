# Reduce() function is useful for performing computation on a list
# Returns a single result, unlike map and filter
# must import functools to use reduce()

from functools import reduce


# ####################################
# TRADITIONAL WAY
# ####################################

starks = ['robb', 'sansa', 'arya', 'eddard', 'jon']


def stark_concat(*args):
    result = ""
    for name in args:
        result += name

    return (result)


print (stark_concat(*starks))


# ####################################
# LAMBDA REDUCE WAY
# ####################################

result = reduce(lambda item1, item2: item1 + item2, starks)
print (result)