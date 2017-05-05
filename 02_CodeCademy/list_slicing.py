# to_five = ['A', 'B', 'C', 'D', 'E']

# print (to_five[3:])
# print (to_five[1:4])
# print (to_five[:4])
# print (to_five[::-1])

# my_list = []

# for i in range(0,11):
#     my_list.append(i)

# print (my_list[1::2])



# ###############

# backwards_by_tens = []

# to_one_hundred = []

# for i in range(101):
#     if i % 10 == 0:
#         backwards_by_tens.append(i)
#         print (i)

# print(backwards_by_tens[::-1])

# # PYTHON 2
# to_one_hundred = range(101)
# backwards_by_tens = to_one_hundred[::-10]
# print (backwards_by_tens)

# ####


to_21 = []
for i in range(1, 22):
    to_21.append(i)

odds = to_21[::2]
print (odds)


middle_third = to_21[7:14]
print (middle_third)
