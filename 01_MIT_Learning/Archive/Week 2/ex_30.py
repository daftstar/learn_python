# Write a Python function, odd, that takes in one number and 
# returns True when the number is odd and False otherwise.


# You should use the % (mod) operator, not if.



# def odd(x):
#     '''
#     x: int

#     returns: True if x is odd, False otherwise
#     '''
#     if x % 2 == 0:
#         return False
#     else:
#         return True



# print(odd(4))



# WITHOUT USING IF STATEMENT


def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    return x % 2 != 0




print(odd(4))
