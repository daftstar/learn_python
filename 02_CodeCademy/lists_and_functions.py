
# def count_small(numbers):
#     total = 0
#     for n in numbers:
#         if n < 10:
#             total += 1
#     return total


# lost = [4, 8, 15, 16, 23, 42]

# print (count_small(lost))



"""
EXERCISE: 

Write a function that counts how many times the string "fizz" appears in a list.

Write a function called fizz_count that takes a list x as input.

Create a variable count to hold the ongoing count. Initialize it to zero.

For each item in x:, if that item is equal to the string "fizz" 
    then increment the count variable.

After the loop, please return the count variable.

For example, fizz_count(["fizz","cat","fizz"]) should return 2.


"""


def fizz_count(x):
    count = 0
    for i in x:
        if i == "fizz":
            count += 1
    return count


print (fizz_count(["fizz", "cat", "fizz"]))


for letter in "Codeacademy":
    print (letter)


print ()
print ()

word = "Programming is fun"

for letter in word: 
    if letter == "i":
        print (letter)