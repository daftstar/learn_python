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
    if is_neg:
        result = '-' + result

    return (result)

print (get_binary(44))  # 101100
print (get_binary(-44))  # -101100