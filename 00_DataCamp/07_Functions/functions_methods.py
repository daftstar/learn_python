# # LIST METHODS
# # .index()

# x = [1, 2, 3, 4, 5, "mom"]
# print (x.index("mom"))

# # In python, everything is an object. 
# # Objects have methods associated to it based on object type

# print("sdfs".index("s"))

# # Functions are called on objects
# print (type(x))

# # Methods call functions on objects
# print (x.index("mom"))

# # string to experiment with: room
room = "poolhouse"

# # Use upper() on room: room_up
room_up = room.upper()

# # Print out room and room_up
# print (room)
# print (room_up)


# # Print out the number of o's in room
# print (room.count("o"))


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print (areas.index(20.0))


# Print out how often 14.5 appears in areas
print (areas.count(14.5))


# Use append twice to add poolhouse and garage size
areas.append(24.5); areas.append(15.45)

# Print out areas
print (areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print (areas)