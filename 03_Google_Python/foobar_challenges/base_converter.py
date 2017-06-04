def base_convert (number, base):

    nums = []
    while number:
        number, r = divmod(number, base)
        nums.append(str(r))
    value = ''.join(reversed(nums))
    return (value)


print (base_convert(210022, 10))

x = 210111
y = 122221

print (x-y)

str_x = str(x)
str_y = str(y)

x = int(str_x, base=3)
y = int(str_y, base=3)

str_z = str(x - y)

print (str_z)
z = "96"

aa = int(z, base=10)
# print (int(str_z, base=3))


# def base_convert (number, base):
#     if number == 0:
#         return '0'
#     nums = []
#     while number:
#         number, r = divmod(number, base)
#         nums.append(str(r))
#     return ''.join(reversed(nums))


# print (base_convert(9, 3))