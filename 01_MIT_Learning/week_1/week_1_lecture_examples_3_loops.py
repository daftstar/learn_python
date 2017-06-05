def new_line():
    print ("\n____________________\n")

# break immediately exits whatever loop it is in. 
# good for loops within loops



"""
# FOR LOOPS
- know number of iterations
- can end early via break
- uses a counter
- can rewrite a for loop using a while loop


# WHILE LOOPS
- unbounded number of iterations
- can end early via break
- can use a counter, but must initialize before loop
  and increment inside loop
- may not be able to rewrite a while loop using a for loop
"""

# mysum = 0

# for i in range(5, 999, 2):
#     mysum += 1
#     print ("mysum:", mysum)
#     print ("i", i)
#     if mysum == 36:
#         break

# print (mysum)

# ######################### EXERCISE ###########################
# EXERCISE: Write a piece of Python code that prints out
# the string 'hello world' if the value of an integer variable,
# happy, is strictly greater than 2.

# happy = 33
# if happy > 2:
#     print ("hello world")



# ######################### EXERCISE ###########################
# Assume that two variables, varA and varB, # are assigned values,
# either numbers or strings. Write a piece of Python code that
# prints out one of the following messages:

# "string involved" if either varA or varB are strings
# "bigger" if varA is larger than varB
# "equal" if varA is equal to varB
# "smaller" if varA is smaller than varB

varA = 7
varB = 3

# be explicit in comparisons
# if type(varA) == str or type(varB) == str:
#     print ("string involved")
# elif varA > varB:
#     print ("bigger")
# elif varA == varB:
#     print ("equal")
# else:
#     print ("smaller")


#####
# num = 0
# while num <= 5:
#     print(num)
#     num += 1

# print("Outside of loop")
# print(num)


#####
# numberOfLoops = 0
# numberOfApples = 2
# while numberOfLoops < 10:
#     numberOfApples *= 2
#     numberOfApples += numberOfLoops
#     numberOfLoops -= 1
# print("Number of apples: " + str(numberOfApples))


num = 10
for num in range(5):
    print(num)
print(num)
new_line()


divisor = 2
for num in range(0, 10, 2):
    print(num / divisor)
new_line()


for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')
new_line()


count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)
new_line()

greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')
new_line()


school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 

