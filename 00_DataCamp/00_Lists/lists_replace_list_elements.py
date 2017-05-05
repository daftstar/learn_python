# x = ["a", "b", "c", "d"]
# x[1] = "r"
# x[2:] = ["s", "3", "asjjs"]

# print (x)


x = ["a", "b", "c", "d"]
y = x + ["e", "f"]

print (y)



areas = [
        "hallway", 11.25,
        "kitchen", 18.0,
        "living room", 20.0,
        "bedroom", 10.75,
        "bathroom", 9.50
        ]

areas[9] = 10.50
print (areas)

areas[4] = "chill zone"
print (areas)

# areas = areas + ["poolhouse", 24.5]
# print (areas)


areas_1 = areas + ["poolhouse", 24.5]
print (areas_1)
areas_2 = areas_1 + ["garage", 15.45]

print (areas_2)