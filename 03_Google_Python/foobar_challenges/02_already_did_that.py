# ########################################################
# CONSTRAINTS
# ########################################################

# Code will run inside a Python 2.7.6 sandbox.
# Standard libraries are supported except for bz2, crypt,
# fcntl, mmap, pwd, pyexpat, select, signal, termios, thread,
# time, unicodedata, zipimport, zlib.

"""
# ########################################################
# INSTRUCTIONS
# ########################################################

# PROBLEM:
# algorithm 

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

# b = 10 # base 10



def answer(n):
    
    count = 0
    last_value = 0

    # y_array = []  # not needed since we can perform operation on x_array
    while n != last_value:
        print ("original value n:", n)
        k = len(str(n))
        string_x = ""
        string_y = ""
        x_array = []
        last_value = n

        for i in str(n):
            x_array.append(i)

        x_array_sorted = sorted(x_array, reverse=True)
        y_array_sorted = sorted(x_array)

        for i in x_array_sorted:
            string_x += i

        for i in y_array_sorted:
            string_y += i

        x = int(string_x)
        y = int(string_y)
        z = x - y

        string_z = str(z).zfill(k)

        n = string_z

        count += 1
        print ("     new value n:", n)
        print ("repetition:", n == last_value)
        print ("total count: ", count)
        print ("\n____________________________\n")
        # return("")



# n = 134833  # infinite loop
n = 320
print (answer(n))
