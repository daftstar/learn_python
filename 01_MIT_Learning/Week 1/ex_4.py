# num = 5
# if num > 2:
#     print(num)
#     num -= 1
# print (num)


# num = 0
# while num <= 5:
#     print(num)
#     num += 1

# print ("Outside of loop")
# print (num)

# #this outputs
# 0
# 1
# 2
# 3
# 4
# 5
# Outside of loop
# 6


# numberOfLoops = 0
# numberOfApples = 2
# while numberOfLoops < 10:
#     numberOfApples *= 2
#     numberOfApples += numberOfLoops
#     numberOfLoops -= 1
# print("Number of apples: " + str(numberOfApples))

### This results in an infinite loop because number of loops will always be < 10


# num = 10
# while num > 3:
#     num -= 1
#     print (num)

# this outputs 9 to 3



######

# num = 10
# while True: 
#     if num < 7:
#         print ("breaking out of the loop")
#         break
#     print (num)
#     num -= 1
# print ('Outside of loop')

# this outputs: 
# 10
# 9
# 8
# 7
# breaking out of the loop
# Outside of loop


# num = 100 
# while not False: 
#     if num > 10:
#         break
# print ('num is: ' + str(num))

######

# num = 10
# for num in range(5):
#     print (num)
# print (num)

# divisor = 2
# for bob in range(0, 10, 2):
#     print(bob / divisor) 

# print("\n")



#########

# for variable in range(20):
#     if variable % 4 == 0:
#         print(variable)
#     if variable % 16 == 0:
#         print('Foo!') 



# THIS OUTPUTS
# 0
# Foo!
# 4
# 8
# 12
# 16
# Foo!



# #########


# myStr = '6.00x'

# for char in myStr:
#     print(char)

# print('done')

# OUTPUTS
# 6
# .
# 0
# 0
# x
# done





# #############
# greeting = 'Hello!'
# count = 0

# for letter in greeting:
#     count += 1
#     if count % 2 == 0:
#         print(letter)
#     print(letter)

# print ('done')

# OUTPUTS
# H
# e
# e
# l
# l
# l
# o
# !
# !
# done

# school = 'Massachusetts Institute of Technology'
# numVowels = 0
# numCons = 0

# for char in school:
#     if char == 'a' or char == 'e' or char == 'i' \
#        or char == 'o' or char == 'u':
#         numVowels += 1
#     elif char == 'o' or char == 'M':
#         print (char)
#     else:
#         numCons -= 1
# print ("vowels: %d " % numVowels)
# print ("Consonents: %d" % numCons)


# OUTPUTS

# M
# vowels: 11 
# Consonents: -25




##### Calculating if a number is a perfect cube
# x = int(input('Enter an integer: '))
# x = -27
# ans = 0

# while ans ** 3 < x:
#     ans = ans + 1
# if ans ** 3 != x:
#     print ("%s is not a perfect cube" % x)
# else:
#     print ("Cube root of %s is %s" % (x, ans))

### THIS ACCOMODATES NEGATIVE VALUES
# cube = -8

# for guess in range(abs(cube)+1):
#     if guess**3 >= abs(cube):
#         break
# if guess ** 3 != abs(cube):
#         print ("%s is not a perfect cube" % cube)
# else:
#     if cube < 0:
#         guess = -guess
#     print ("Cube root of %s is %s" % (cube, guess))



### !!!!!!!!!!!
### ALWAYS REMEMBER TO DECLARE VARIABLES OUTSIDE OF LOOPS!!! ###
### Otherise, the loop cannot append to the variable. 

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
print("#########################\n")

## ANOTHER WAY TO DO THIS: 
print ("Here's another way to do this")
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
print("#########################\n")


### AND ANOTHER WAY
print("And, here's another another way")

count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
print("#########################\n")



### FINALLY, the simplest way
print ("here's this simplest way")
count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    







