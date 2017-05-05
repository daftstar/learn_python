# WHILE LOOPS


# offset = 0

# while offset != 0:
#     print ("correcting...")
#     if offset > 0:
#         offset -= 1
#     else:
#         offset += 1
#     print (offset)


# # FOR LOOPS (iterations)

# fam = [1.73, 1.68, 1.71, 1.89]

# # for i in fam:
# #     print (i)

# # OR

# for i, x in enumerate(fam):
#     # print (i, x)
#     print ("index " + str(i) + ": " + str(x))


# for i in "FAMILY":
#     print (i)


# # areas list
# areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# # Change for loop to use enumerate()
# for x, y in enumerate(areas):
#     x += 1  # avoid index = 0
#     print("room " + str(x) + ": " + str(y))

# __________________________________________


house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

for x,y  in house:
    # print (x, y)
    print ("the %s is %s sqm" % (x, y))