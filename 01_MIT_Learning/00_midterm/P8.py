# Write a function called general_poly,
# that meets the specifications below.
#
# For example, general_poly([1, 2, 3, 4])(10)
# should evaluate to 1234 because:
# 1*10^3 + 2*10^2 + 3*10^1 + 4*10^0


def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def add_calc(x):
        evaluate = 0
        # for each int in L, update the value of evaluate by
        # multiplying current value of evaluate by x(base) and then
        # add the integer (i).
        #  e.g. x = 10, L = [1, 2, 3, 4]
        # (0*10 + 1) = 1
        # 1 * 10 + 2 = 12
        # 12 * 10 + 3 = 123
        # 123 * 10 + 4 = 1234
        for i in L:
            evaluate = (evaluate * x) + i
        return evaluate
    return add_calc


print (general_poly([1, 2, 3, 4])(10))




# WORKS BACKWARDS, BUT DOESN'T PASS TESTING HARNESS ON MIT. 
x = 10 
def general_poly(L):
    """
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x,
    returns the value:
        n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    """
    def add_calc(x):
        # x = 10
        length = len(L) - 1
        evaluate = 0

        if len(L) == 1:
            return L[0]

        for i in range(len(L)):
            evaluate += (L[i] * (x ** length))
            length -= 1
            # print (L[i], evaluate)

        return evaluate
    return (add_calc(x))


# print (general_poly([1, 2, 3, 4]))

L = [1, 2, 3, 4]


# print (general_poly(L))
















# x = 10 
# def general_poly(L):
#     """
#     L, a list of numbers (n0, n1, n2, ... nk)
#     Returns a function, which when applied to a value x,
#     returns the value:
#         n0 * x^k + n1 * x^(k-1) + ... nk * x^0
#     """
#     def add_calc(x):
#         # x = 10
#         length = len(L) - 1
#         evaluate = 0

#         if len(L) == 1:
#             return L[0]

#         for i in range(len(L)):
#             evaluate += (L[i] * (x ** length))
#             length -= 1
#             # print (L[i], evaluate)

#         return evaluate
#     return (add_calc(x))


# print (general_poly([1, 2, 3, 4]))


# # L = [5, 6, 7, 8, 9]
# L = [1, 2, 3, 4]
# # L = [9]

# print (general_poly(L))







# def general_poly(L, x):
#     """
#     L, a list of numbers (n0, n1, n2, ... nk)
#     Returns a function, which when applied to a value x,
#     returns the value:
#         n0 * x^k + n1 * x^(k-1) + ... nk * x^0
#     """
#     length = len(L) - 1
#     evaluate = 0

#     if len(L) == 1:
#         return L[0]

#     for i in range(len(L)):
#         evaluate += (L[i] * (x ** length))
#         length -= 1
#         print (L[i], evaluate)

#     return (evaluate)


# # L = [5, 6, 7, 8, 9]
# L = [1, 2, 3, 4]
# # L = [9]

# print (general_poly(L, 10))




# Answers:
# 1234
# 4
# 3
# 380
# 189
# 2.6875
# 335.2






# def general_poly(L, x):
#     """
#     L, a list of numbers (n0, n1, n2, ... nk)
#     Returns a function, which when applied to a value x,
#     returns the value:
#         n0 * x^k + n1 * x^(k-1) + ... nk * x^0
#     """
#     length = len(L) - 1
#     evaluate = 0

#     if len(L) == 1:
#         return L[0]

#     for i in range(len(L)):
#         evaluate += (L[i] * (x ** length))
#         length -= 1

#     return (evaluate)
