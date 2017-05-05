# suitcase = []
# # contents = "memory", "carbonic glasses", "flashlight"


# """
# THIS IS A TUPLE
# contents = "memory", "carbonic glasses", "flashlight"
# """


# """
# THIS IS A LIST / ARRAY
# contents = ["memory", "carbonic glasses", "flashlight"]
# print (type(contents))

# """


# suitcase.append("sunglasses")
# suitcase.append("wiggles")
# suitcase.append("333")


# list_length = len(suitcase)
# # Set this to the length of suitcase

# print ("There are %d items in the suitcase." % (list_length))
# print (suitcase)


"""
SPLICING
"""

# suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# first  = suitcase[0:2]  # The first and second items (index zero and one)
# middle = suitcase[2:4]               # Third and fourth items (index two and three)
# last   = suitcase[4:6]           # The last two items (index four and five)


# print (first)
# print (middle)
# print (last)


# animals = "catdogfrog"
# cat  = animals[:3]      # The first three characters of animals
# dog  = animals[3:6]     # The fourth through sixth characters
# frog = animals[6:]      # From the seventh character to the end

# print (cat)
# print (dog)
# print (frog)


"""
LIST INSERTIONS
"""

# animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
# duck_index = animals.index("duck")
# animals.insert(duck_index, "cobra")

# print (duck_index)
# print (animals)

# for i in animals:
#     print (i)


start_list = [5, 3, 1, 2, 4]
square_list = []

for x in start_list:
    x = x **2
    square_list.append(x)

square_list.sort()
print (square_list)



