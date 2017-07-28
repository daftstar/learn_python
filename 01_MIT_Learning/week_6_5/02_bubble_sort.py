# BUBBLE SORT
# compare consecutive pairs of elements
# swap elements in pair such that smaller is first
# when reach end of the list, start over again
# stop where no more swaps have been made


def bubble_sort(L):
    swap = False
    count = 0
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:   # to avoid index error
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                print (L)
                count +=1
    return count


L = [1, 2, 3, 4, 5, 1000, 16, 2, 3, 9, 2, 22, 44, 14, 7]
print (bubble_sort(L))

# inner for loop is doing the comparisons
# outer while sloop is for doing multiple passes until no more swaps
# O(n^2) where n is len(L)
# to do len(L)-1 comparisons and len(L)-1 passes
