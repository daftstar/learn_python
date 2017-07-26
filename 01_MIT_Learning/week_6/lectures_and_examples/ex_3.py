def program1(L):
    multiples = []
    for x in L:
        for y in L:
            multiples.append(x*y)
    return multiples

L = []
# L = [3, 6, 9, 10, 12, 11, 13, 15]
print (program1(L))

# best case scenario is empty list = 2 steps
# worst case scenario is loop within loop x list size = n+2 +(3*n^2)


def program2(L):
    squares = []                        # step 1
    for x in L:                         # step 2
        for y in L:                     # step 3
            if x == y:                  # step 4
                squares.append(x*y)     # step 5
    return squares


L = []
# L = [3, 6, 9, 10, 12, 11, 13, 15]
print (program2(L))

# best case = 2 steps
# worst case = n+2 + (4*n^2)


def program3(L1, L2):
    intersection = []                   # step 1 w/ empty L1
    for elt in L1:
        if elt in L2:
            intersection.append(elt)
    return intersection                 # step 2 w/ empty L1


L1 = []
L2 = []
print (program3(L1, L2))

#                  # 2 lists + 2 steps + 2 nested loops
# worst case scenario = (2*n + 2) + n^2



