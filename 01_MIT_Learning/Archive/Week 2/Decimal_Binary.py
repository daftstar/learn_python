# # ### CONVERTING INT TO BINARY ###

isNeg = False

num = 11
origNum = num
result = ''


if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

if num == 0:
    result = '0'

while num > 0:
    result = str(num % 2) + result
    print ("The current representation of %s is %s" % (num, result))
    num = num // 2


if isNeg:
    result = '-%s' % result
    print ("The current representation of %s is %s" % (num, result))
print("____________________________________________________")
print ("The binary representation of %s is %s" % (origNum, result))

print (" \n#########################################################\n")


# ### CONVERTING FLOAT TO BINARY ###

x = .11
p = 3
result = ''

# print (.44 % 1)
# print (((2 ** p) * x)%1 )



# # part1 = str((2 ** p) * x)
# # part2 = int((2 ** p) * x)

# # print ("Float Value (part 1) is: %s" % part1) 
# # print ("Base Number (part 2) is: %s" % part2)


while ((2 ** p) * x)%1 != 0:
    print ("Remainder = " + str((2 ** p) * x - int((2 ** p) * x)))
    p += 1

num = int(x * (2 ** p))

if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2

for i in range(p - len(result)):
    result = '0' + result

    result = result[0: -p] + '.' + result[-p:]
    
print ("The binary representation of the decimal " + str(x) + " is " + result)









