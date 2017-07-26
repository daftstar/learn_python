def linearSearch(L, x):
    position = None
    for e in L:
        if e == x:
            position = L.index(x)
            print()
            print ("position of %s is: %s " % (e, position))
            return True
    print()
    print ("position of %s is: %s " % (e, position))
    return False


# Best case runtime is where e == x on first go.
print (linearSearch([20, 10, 1, 7, 4, 22, 25, 12, 31], 20))

# worst case is where need to get to end of list to find e == x
# or not found at all
print (linearSearch([21, 1, 25, 22, 30, 13, 7, 24, 12], 24))
print (linearSearch([21, 1, 25, 22, 30, 13, 7, 24, 12], 26))


# average case is where e == x is somewhere in the middle
print(linearSearch([9, 3, 12, 24, 7, 8, 23, 11, 19], 8))
print(linearSearch([4, 12, 20, 17, 9, 14, 7, 24, 6], 7))


# What is the number of steps it will take to run
# linearSearch in the best case?
# In terms of n, the number of elements in the list L
# best case, found in first runtime... first element in L
# 1

# What is the number of steps it will take to run
# linearSearch in the word case?

# In the worst case scenario, x is not present in L.
# Thus we go through the for loop n times.
# This means we execute assignment of e to each element of L
# (this takes place in the line for e in L) to enter
# the for loop, and also execute the check

# (2 * n) + 1

def program1(x):
    total = 0
    for i in range(1000):
        total += 1
        # print (total)

    while x > 0:
        x -= 1
        # print (x)
        total += x
        # print (total)

    return total


print (program1(20))
print()

# Best Case: x is less than or equal to 0.
# We first execute the assignment total = 0 for one step.
# Next we execute the for i in range(1000) loop.
# This loop is executed 1000 times and has three steps
#     (one for the assignment of i each time through the loop,
#     as well as two for the += operation) on each iteration.

# We next check if x > 0 - it is not so we do not enter the loop.
# Adding one more step for the return statement,
# in the best case we execute 1 + 3*1000 + 1 + 1 = 3003 steps.


# In the worst case scenario, x is a large positive number.
# In this case, we first execute the assignment total = 0
# for one step. Next we execute the first loop 1000 times
#     (3000 total steps),

# Then we execute the second loop (while x > 0) n times.
# This loop has five steps (one for the conditional check, x > 0,
#         and two each for the -= and += operations).
# When we finally get to the point where x = 0,
# we execute the conditional check x > 0 one last time
#     - since it is not, we do not enter the loop.
# Adding one more step for the return statement,
# in the worst case we execute
#     1 + 3*1000 + 5*n + 1 + 1 = 5*n + 3003 steps.


# ##########################
def program2(x):
    total = 0
    for i in range(1000):
        total = i

    while x > 0:
        x = x//2
        total += x

    return total


print (program2(4))


# In the best case scenario, x is less than or equal to 0.
# We first execute the assignment total = 0 for one step.
# Next we execute the for i in range(1000) loop.
# This loop is executed 1000 times and has two steps
# (one for the assignment of i each time through the loop,
#     as well as one for the = operation) on each iteration.

# We next check if x > 0 - it is not so we do not enter the loop.
# Adding in one step for the return statement, in the best case
# we execute 1 + 2*1000 + 1 + 1 = 2003 steps.

#
#
def program3(L):
    totalSum = 0
    highestFound = None
    for x in L:
        totalSum += x

    for x in L:
        if highestFound is None:
            highestFound = x
        elif x > highestFound:
            highestFound = x

    return (totalSum, highestFound)


# In the best case scenario, L is an empty list.
# Thus we execute only the first two assignment statements,
# then the return statement.
# Therefore in the best case we execute 3 steps.
# Note that since the list is empty, no assignments are performed
# in the for x in L lines.
# In the worst case scenario, L is a list with its elements
# sorted in increasing order (eg, [1, 3, 5, 7, ...]).

# In this case we execute the first two assignment statements
#     (2 steps).

# Next we execute the first loop n times.
# This first loop has three steps
#     (one for the assignment of x each time through the loop,
#     as well as two for the += operation),adding 3*n steps.

# Finally we execute the second loop n times.
# The first time we execute this loop, we perform 3 steps
# - one for the assignment of x; then we run the check
# if highestFound == None, and finding it to be True,
# we execute the assignment highestFound = x.

# The next (n-1) times we execute this loop, we perform 4 steps:
# one for the assignment of x, then we run the check if
# highestFound == None, and finding it to be False,
# we run the check elif x > highestFound.

# Since this is always True (the list is sorted in
# increasing order), we execute the assignment highestFound = x.
# Therefore in the second loop we execute
#     3 + (n-1)*4 = 3 + 4*n - 4 = 4*n - 1 steps.

# Finally we execute the return statement,
# which is one more step.

# Pulling this all together, we can see that in the
# worst case we execute
#     2 + 3*n + 4*n - 1 + 1= 7*n + 2 steps.
