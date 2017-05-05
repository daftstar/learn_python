# x = ["a", "b", "c", "d"]
# print (x)
# DELETING LIST ELEMENTS
# del (x[1])
# print (x)


# areas = [
#         "hallway", 11.25,
#         "kitchen", 18.0,
#         "chill zone", 20.0,
#         "bedroom", 10.75,
#         "bathroom", 10.50,
#         "poolhouse", 24.5,
#         "garage", 15.45
#         ]

# del (areas[10]); del (areas[10])  # OR
# del(areas[-4:-2])
# print (areas)


areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = areas
print (id(areas))
print (id(areas_copy))
# When you do this, two lists point to the same values. 
# Create an explicit list copy using [:] or list()
print()

areas_copy = list(areas)  # OR YOU CAN USE THE BELOW
# areas_copy = areas[:]

print (id(areas))
print (id(areas_copy))