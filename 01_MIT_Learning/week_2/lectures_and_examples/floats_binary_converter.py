"""
Floats approximate real numbers. 
302 = 3*10^2 + 0*10^1 + 2*10^0
    = 300 + 0 + 2
    = 302

 Binary is the same thing
 10011 = 1*2^4 + 0*2^3 + 0*2^2 + 1*2^1 + 1*2^0
       =    16 +   0   +   0   +   2   +   1
       = 19
"""




def get_binary(num):
    if num < 0:
        is_neg = True
        num = abs(num)
    else:
        is_neg = False

    result = ""

    if num == 0:
        result = '0'
    while num > 0:
        result = str(num % 2) + result
        num = num//2
        print ("last digit + prev result: %s" % result)
    if is_neg:
        result = '-' + result

    return (result)

print (get_binary(11))  # 101100
print ("")

# ####################################
# WORKING WITH FLOATS / FRACTIONS #
# ####################################
"""
3/8 = 0.375 = 3*10^-1 + 7*10^-2 + 5*10^-3
            =    .3   + .07     + .005
 3 / 8 = .375
 3 = .375 * 8
 3 = .375 * 2*2^3
 3 in binary = 11
    (3 % 2) + (1 % 2)

"""


def conv_float(x):
    p = 0
    while ((2 ** p) * x) % 1 != 0:
        print('Remainder = ' + str((2 ** p) * x - int((2 ** p) * x)))
        p += 1
        num = int(x*(2**p))

    result = ''
    if num == 0:
        result = '0'

    while num > 0:
        result = str(num % 2) + result
        num = num//2

    for i in range(p - len(result)):
        result = '0' + result

    result = result[0:-p] + '.' + result[-p:]
    return('The binary representation of the decimal ' + str(x) + ' is ' + str(result))


print (conv_float(.1))


# When testing equality of floats, 
# Use abs(x-y) < some small number, rather than x == y
