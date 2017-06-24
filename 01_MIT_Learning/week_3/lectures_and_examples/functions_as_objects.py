# functions are first class objectss
# has types
# can be elements of data structures
# can appear within expressions, i.e. using function as arguments

testList = [1, -4, 8, -9]

# Mutates data of existing list
# def apply_to_each(data, func_name):
#     for i in range(len(data)):
#         testList[i] = func_name(data[i])
#     return ("")

# returns a mutated list, original stays in tact
# def apply_to_each(data, func_name):
#     new_list = []
#     for i in data:
#         new_list.append(func_name(i))
#     return (new_list)


# def applyToEach(L, f):
#     for i in range(len(L)):
#         L[i] = f(L[i])


# # def plus_one(a):
# #     return a + 1


# def square(a):
#     return abs(a ** 2)

# applyToEach(testList, square)


def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result


def square(a):
    return a*a


def halve(a):
    return a/2


def inc(a):
    return a+1

print (applyEachTo([inc, square, halve, abs], -3))
print (applyEachTo([inc, square, halve, abs], 3.0))
# print (applyEachTo([inc, max, int], -3))