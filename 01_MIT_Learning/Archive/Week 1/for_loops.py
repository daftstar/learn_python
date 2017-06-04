
### EXERCISE 1
# 1. Convert the following code into code that uses a for loop.

# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints "Goodbye!"


# mynum = 0
# for i in range(0, 10, 2):
#     mynum += 2
#     print (mynum)
# print ("Goodbye!")


#ALTERNATIVELY, YOU COULD WRITE THIS:
# for count in range(2, 12, 2):
#     print(count)
# print ("Goodbye")





### EXERCISE 2
# 2. Convert the following code into code that uses a for loop.

# prints "Hello!"
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2



# mynum = 12
# print ("Hello!")
# for i in range(0, 10, 2):
#     mynum -= 2
#     print (mynum)
# # print ("\n######\n")

# print ("Hello")
# for num in range (10, 0, -2):
#     print (num)

# you can use 'num' or 'count', both work as the same variable


### EXERCISE 3
# 3. Write a for loop that sums the values 1
# through end, inclusive. end is a variable that we 
# define for you. So, for example, if we define end 
# to be 6, your code should print out the result:

# 21
# which is 1 + 2 + 3 + 4 + 5 + 6.

# For problems such as these, do not include input statements or define variables we will provide for you. Our automating testing will provide values so write your code in the following box assuming these variables are already defined.




# end = 6
# for i in range(0, end):
#     end += i
#     print ("the current value of 'end' is: %s" % end)
# print (end)

# for everytime i count is between 0 and "end", which is 6,
#   take the value of end, and increase it by the current value of i.
#   comtinue doing this until you get to the value of end, which is 6
#   this should result in 
# 6 + 0 = 6
# 6 + 1 = 7
# 7 + 2 = 9
# 9 + 3 = 12
# 12 + 4 = 16
# 16 + 5 = 21




