# MERGE SORT


# # use a divide and conquer method
# 1. if list of length of 0 or 1, it's already sorted
# 2. if list has more than one element, split into two lists
#   and sort each one.
# 3. merge sorted sublists
#   a) look at first element of each, move smaller
#      to end of result
#   b) when one list is empty, copy rest of other list
"""
|_________________________________________________| # UNSORTED

|_______________________| |_______________________| # UNSORTED

|__________| |__________| |__________| |__________| # UNSORTED

|___| |___|  |___| |___|   |___| |___|  |___| |___| # SORTED

|__________| |__________| |__________| |__________| # SORTED MERGED

|_______________________| |_______________________| # SORTED MERGED


L = [1,5,12,18,19,20,2,3,4,1]

Left in list 1      Left in list 2  Compare     Result
[1,5,12,18,19,20]   [2,3,4,17]        1, 2       []
[5,12,18,19,20]     [2,3,4,17]        5, 2       [1]
[5,12,18,19,20]     [3,4,17]          5, 3       [1,2]
[5,12,18,19,20]     [4,17]            5, 4       [1,2,3]
[5,12,18,19,20]     [17]              5, 17      [1,2,3,4]
[12,18,19,20]       [17]              12, 17     [1,2,3,4,5]
[18,19,20]          [17]              18, 17     [1,2,3,4,5,12]
[18,19,20]          []                18, --     [1,2,3,4,5,12,17]
[]                  []                           [1,2,3,4,5,12,17,18,19,20]
"""


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while (i < len(left)):
        result.append(left[i])
        i += 1

    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

L = [1, 2, 3, 4, 5, 1000, 16, 2, 3, 9, 2, 22, 44, 14, 7]
print (merge_sort(L))

# overall complexity is O(n log(n)) where n is len(L)

# LINEAR sort
#   O(log n)
# BOGO sort
#   randomness, unbounded O()

# BUBBLE sort
#   O(n2)

# SELECTION sort
#   O(n2)
#   guaranteed the first i elements were sorted

# MERGE sort
#   O(n log(n))

# O(n log(n)) is the fastest a sort can be
