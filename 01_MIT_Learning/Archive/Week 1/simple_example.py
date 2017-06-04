
# SIMPLE CONDITIONAL EXAMPLE
# x = 52

# if x % 2 == 0:
#     print ('')
#     print ('Even')
# else:
#     print('')
#     print('Odd')

# print ('Done with condisiotnal')



# NESTED CONDITIONAL EXAMPLE

# x = 289

# if x % 2 == 0:
#     if x % 3 == 0:
#         print ("Divisible by 2 and 3")
#     else:
#         print ("Divisible by 2, and NOT 3")

# elif x % 3 == 0:
#     print ('Divisible by 3, and NOT by 2')

# elif x % 3 != 0:
#     print ("your number is not divisible by 2 or 3")


# COMPOUND BOOLEANS

# x = 10
# y = 8
# z = 9

# if x < y and x < z:
#     print ('x is least')
# elif y < z: 
#     print ('y is least')
# else:
#     print ('z is least')


# if 6 > 7:
#    print("Yep")


# FOR LOOP

# n = 2

# while n < 5:
#     print(n)
#     n += 1
#     # n = n + 1


# WHILE LOOP THAT DOES THE SAME THING
# a = -13
# for z in range(5):  # range only works with + numbers? 
#     print(z)


# ##################################

# RANGE STATEMENTS & LOOPS
# RANGE (start, stop, step)


# this program will do the following: 
# start with 0, then add continue to add the values from 7 until 10
# thus, the output will be 
# ( 0 + 7 ) = 7
# ( 7 + 8)  = 15
# (15 + 9)  = 24

# mysum = 0
# for i in range(7, 10):  # to specifiy range of values vs. all
#     mysum += i
#     print (mysum)

# --------------------------------


# this program will do the following: 
# start with 0, then add continue to add the values from 5 until 11, in increments of 2
# thus, the output will be 
# ( 0 + 5 ) = 5
# ( 5 + 7)  = 12
# (12 + 9)  = 21
# (21 + 11 ) ---- LIMIT REACHED. STOP INCREMENT. 


# number = 0

# for i in range(5, 11, 1):
#     number += i
#     print (number)

# i is a system / global variable

# ##################################
# BREAK STATEMENTS

myValue = -333
for i in range(1, 100, 2):
    myValue += i
    print(myValue)
    if myValue >= 10:
        break
    

print ("here you go: %s, what a cool number huH? " % myValue)









