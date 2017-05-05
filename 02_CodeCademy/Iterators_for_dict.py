my_dict = {
    "Apple": "Okay",
    "Orange": "Good",
    "Stone Fruit": "Excellent"
}

# print (my_dict.items())
# print ("")
# print (my_dict)
# print ("")


# ACCESSING KEYS AND VARIABLES USING BUILT-IN FUNCTIONS
"""
print (my_dict.keys())
print (my_dict.values())


for i in my_dict.keys():
    print (i)

print ("")

for i in my_dict:
    print (i)

for i in my_dict:
    print (my_dict[i])

for i in my_dict:
    print (i, my_dict[i])

"""


"""
# BUILDING LISTS THROUGH LIST COMPREHENSION
"""

# evens_to_50 = [i for i in range(51) if i % 2 == 0]
# print (evens_to_50)

even_squares = [i ** 2 for i in range(1,11) if i % 2 == 0]
print (even_squares)

# Comprehension should consist of:
#   cubes of numbers, 1 to 10
#   ONLY if cube is evenly divisible by 4

cubes_by_four = [i ** 3 for i in range(1, 11) if ((i ** 3) % 4) == 0]
print (cubes_by_four)

