import random
random.seed(a=11, version=2)

# create new list
L = [random.randint(1, 1400) for i in range(1000)]

# create sorted version of L
SL = L.copy()
SORTED = sorted(L)


# _________________________________________________________________

# LINEAR SEARCH ON UNSORTED LIST
# Brute Force Search
# List does not have to be sorted

def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
            print ("found at position: ", i)
    return found


print (linear_search(L, 1))
print ()

# must look through all elements to decide it’s not there
# O(len(L)) for the loop * O(1) to test if e == L[i]
# Overall complexity is linear, O(n) where n is len(L)


# _________________________________________________________________
# LINEAR SEARCH ON SORTED LIST

def search(SORTED, e):
    for i in range(len(SORTED)):
        # run through list until match is found
        if SORTED[i] == e:
            return (SORTED[i], "found at position: ", i)
        # starting from the beginning, if the value in the sorted list is
        # higher than e, then we can immediately break the loop
        if SORTED[i] > e:
            return False


print (search(SORTED, 129))
print (search(SORTED, 402))
print()

# Overall complexity is still O(n), where n is len(L) -
#   worst case scenario is that e is not found in list,
#   still had to iterate through entire list


# _________________________________________________________________
# BISECTION SEARCH ON SORTED LIST (REQUIRES SORTED LIST)
def bisect_search(SORTED, e):
    if SORTED[-1] < e:                                          # constant O(1)
        print ("largest value in list is:", SORTED[-1])
        return ("value %s out of bounds" % e)

    if SORTED == []:                                            # constant O(1)
        return False

    elif len(SORTED) == 1:                                      # constant O(1)
        # print ("length of SORTED is:", len(SORTED))
        print ("value at end is: ", SORTED[0])
        return SORTED[0] == e
    else:
        half = len(SORTED)//2                                   # constant O(1)
        print ("current half is:", half)
        if SORTED[half] > e:
            return bisect_search(SORTED[:half], e)              # O(log n), where n is len(SORTED) - this creates copies of the list, which dramatically adds complexity
        else:
            return bisect_search(SORTED[half:], e)              # O(log n), where n is len(SORTED) - this creates copies of the list, which dramatically adds complexity


print (bisect_search(SORTED, 21093))


# ALTERNATE VERSION OF BISECTION SEARCH
def bisect_search2(SORTED, e):
    def bisect_search_helper(SORTED, e, low, high):
        if high == low:
            return SORTED[low] == e
        
        mid = (low + high)//2
        if SORTED[mid] == e:
            return True
        elif SORTED[mid] > e:
            if low == mid:      # nothing left to search
                return False
            else:
                return bisect_search_helper(SORTED, e, low, mid-1)
        else:
            return bisect_search_helper(SORTED, e, mid + 1, high)

    if len(SORTED) == 0:
        return False
    else:
        return bisect_search_helper(SORTED, e, 0, len(SORTED) - 1)

# print (SORTED)
print (bisect_search2(SORTED, 1390))

# complexity of both is still O(log n)
# in bisect2, pass list and indices as parameters
# list is never copied, just re-passed


# Only makes sense to sort first, then search if:
# SORT + O(log n) < O(n) >> SORT < O(n) - O(log n)
# Unfortunately, sorting is never less than O(n)

# however, if multiple calls will be made on a sorted list,
# then it is worth sorting the list - cost becomes ammortized

