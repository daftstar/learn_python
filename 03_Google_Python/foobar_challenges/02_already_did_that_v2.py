# ########################################################
# CONSTRAINTS
# ########################################################

# Code will run inside a Python 2.7.6 sandbox.
# Standard libraries are supported except for bz2, crypt,
# fcntl, mmap, pwd, pyexpat, select, signal, termios, thread,
# time, unicodedata, zipimport, zlib.

"""
# ########################################################
# PROBLEM & INSTRUCTIONS
# ########################################################

# PROBLEM:
# algorithm gets into an infinite loop, based on starting n

# INSTRUCTIONS
# 1) Start with a random minion ID n,
#    which is a nonnegative integer of length k in base b

# 2) Define x and y as integers of length k.
#    x has the digits of n in descending order,
#    and y has the digits of n in ascending order

# 3) Define z = x - y.
#    Add leading zeros to z to maintain length k
#    if necessary

# 4) Assign n = z to get the next minion ID,
#   and go back to step 2.
"""

# ########################################################
# TEST EXAMPLES
# ########################################################

# given minion ID
#     n = 1211,
#     k = 4,
#     b = 10

#     then
#     x = 2111,
#     y = 1112 and
#     z = 2111 - 1112 = 0999.

#     Then the next minion ID will be
#     n = 0999 and the algorithm iterates again:
#     x = 9990, y = 0999 and z = 9990 - 0999 = 8991,
#     and so on.



def change_ary(num, base):
    
    if base <= 1:
        return

    if num < 0:
        is_neg = True
        num = abs(num)

    else:
        is_neg = False

    result = ""

    if num == 0:
        result = '0'
    while num > 0:
        result = str(num % base) + result
        num = num//base
    if is_neg:
        result = '-' + result

    return (int(result))


value = (change_ary(44, 2))
print (value, type(value))


# def answer(n, b):



