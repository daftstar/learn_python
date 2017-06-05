def new_line():
    print ("\n____________________\n")

# ######################### EXERCISE 1 ###########################
# Assume that two variables, varA and varB, # are assigned values,
# either numbers or strings. Write a piece of Python code that
# prints out one of the following messages:

# 1. Convert the following into code that uses a while loop.

# print 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!


num = 0
while True:
    if num > 8:
        print ("Goodbye!")
        break
    num += 2
    print (num)

# OR

num = 0
while num < 10:
    num += 2
    print (num)
print ("Goodbye!")


new_line()


# ######################### EXERCISE 2 ###########################
# Convert the following into code that uses a while loop.

# prints Hello!
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2

x = 10
print ("Hello!")

while x > 0:
    print (x)
    x -= 2
new_line()

# ######################### EXERCISE 3 ###########################
# Write a while loop that sums the values 1 through end, inclusive.
# end is a variable that we define for you.

# So, for example, if we define end to be 6, your code should
# print out the result: 21, which is 1 + 2 + 3 + 4 + 5 + 6

end = 6

while end > 0:
    sum_value = 0

    for i in range(1, end + 1):
        # print (i)
        sum_value += i
        end -= 1
    print (sum_value)
new_line()


# Without using FOR or RANGE

end = 6

sum_value_2 = end
while end > 0:
    end -= 1
    sum_value_2 += end
    
print (sum_value_2)
new_line()

# ######################### EXERCISE 4 ###########################

# 1. Convert the following code into code that uses a for loop.

# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints "Goodbye!"

for i in range(2, 12, 2):
    print (i)
print ("Goodbye!")
new_line()


# ######################### EXERCISE 5 ###########################
# Convert the following code into code that uses a for loop.

# prints "Hello!"
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2

print ("Hello!")
for i in range (10, 0, -2):
    print (i)
new_line()


# ######################### EXERCISE 6 ###########################
# Write a for loop that sums the values 1 through end,
# inclusive. end is a variable that we define for you.
# So, for example, if we define end to be 6,
# your code should print out the result: 21
# which is 1 + 2 + 3 + 4 + 5 + 6.


end = 6
new_sum = 0

for i in range(end + 1):
    new_sum += i
print (new_sum)
new_line()


# ######################### EXERCISE 7 ###########################
# Code Evaluation

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
new_line()


count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))