import random
# import shuffle

# monkey sort is random sort until it's sorted correctly
# Quantum mechanics ... :)

def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)
    # return count


L = [4, 3, 1, 99, 31, 16]
# print (bogo_sort(L))
# best case: O(n) where n is len(L) to check if sorted
# worst case: O(?) it is unbounded if really unlucky