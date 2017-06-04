# answer = 0
# neg_flag = False

# # x = int(input("Enter an integer: "))
# x = 1089

# if x < 0:
#     neg_flag = True

# while answer ** 2 < x:  # ALWAYS REMEMBER WHILE = LOOP UNTIL TRUE
#     answer += 1
#     print ("guessing if %s is the sqrt of x" % answer)

# if answer ** 2 == x:
#     print ("Square root of %s is %s" % (x, answer))
# else:
#     print ("%s is not a perfect square" % x)
#     if neg_flag == True:
#         print ("Just checking... did you mean %s?" % -x)


# s = "iii uuu oodkdkd iii"

# for index in range(len(s)):
#     if s[index] == 'i' or s[index] == 'u':
#         print ("There is an i or a u at point %s" % index)

# print ("################")

# for char in s:
#     if char == 'i' or char == 'u':
#         print ("There is an i or u")


# an_letters = "aefhilmnorsxAEFHILMNORSX"


# word = "MIT"
# times = 4

# i = 0

# while i < len(word):
#     char = word[i]
#     if char in an_letters:
#         print ("Give me an %s! %s" % (char.upper(), char))
#     else:
#         print ("Give me a %s! %s" % (char.upper(), char))
#     i += 1


# print ("What does that spell?")

# for i in range(times):
#     print ("%s !!!!" % word)


iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print ("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1




# ############## This won't work because the variable is defined within the function
print ("############")

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 


# ############## DIVIS in scope
print ("\n\n#####DIVIS in scope #######")


iteration = 0

while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 



# ############## DIVIS OUT scope
print ("\n\n#####DIVIS OUT scope #######")


iteration = 0
count = 0

while iteration < 5:

    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 




    
