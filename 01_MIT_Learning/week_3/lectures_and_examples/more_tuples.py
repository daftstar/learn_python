t1 = (1, 'two', 3)
t2 = (t1, 3.25)

print (t1)
print (t2)
print ()
print ((t1 + t2))
print (t1 + t2)

print ((t1 + t2)[2])
print ((t1 + t2)[3])
print ((t1 + t2)[2:5])
print ()


def intersect(t1, t2):
    """
    Assumes t1 and t2 are tuples
    Returns a tuple containing elements
    that are in both t1 & t2
    """

    result = ()
    for e in t1:
        if e in t2:
            result += (e,)  # signifies tuple

    return (result)

tuple1 = (33, 11, 9, 19, "a")
tuple2 = ("a", 33, 19, 6)

print (intersect(tuple1, tuple2))
print ()


# sequences and multiple assignment
def findExtremeDivisor(n1, n2):
    """
    Assume that n1, n2 are positive integers
    Returns a tuple containing smallest common divisor > 1
    and largest common divisor of n1 and n2. If no common
    divisor, returns (None, None)
    """

    minVal, maxVal = (None, None)
    for i in range (2, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            if minVal == None:
                minVal = i
            maxVal = i
    return (minVal, maxVal)

print (findExtremeDivisor(30, 210))

minDivisor, maxDivisor = findExtremeDivisor(30, 210)
print (minDivisor)
print (maxDivisor)