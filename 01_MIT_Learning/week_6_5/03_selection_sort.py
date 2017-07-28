# SELECTION SORT

# 1) extract minimum element
# 2) swap it with element at index 0

# 3) in remaining sublist, extract minimum element
# 4) swap it with element at index 1

# 4) keep the left portion of the list sorted
# 5) at ith step, first i elements in list are sorted
# 6) all other elements are bigger than first i elements

def selection_sort(L):
    suffixSt = 0
    count = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
                # print (L)
                count += 1
        suffixSt += 1

    return (L, "count:", count)


L = [1, 2, 3, 4, 5, 1000, 16, 2, 3, 9, 2, 22, 44, 14, 7]
print (selection_sort(L))
print ()

# outer loop executes len(L) times
# inner loop executes len(L) - i times
# complexity of selection sort is: O(n^2) where n is len(L)


def selSort(L):
    count = 0
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
                count +=1
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
    return (L, "count:", count)


L = [1, 2, 3, 4, 5, 1000, 16, 2, 3, 9, 2, 22, 44, 14, 7]
print (selSort(L))
print ()


def newSort(L):
    count = 0
    for i in range(len(L) - 1):
        j = i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
                count += 1
            j += 1
    return (L, "count:", count)

L = [1, 2, 3, 4, 5, 1000, 16, 2, 3, 9, 2, 22, 44, 14, 7]
print (newSort(L))
print ()