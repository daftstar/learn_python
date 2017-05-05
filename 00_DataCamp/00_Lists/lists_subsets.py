# x = ["a", "b", "c", "d"]
# print (x[1])
# print (x[-3])  # same result!


# areas = ["hallway", 11.25, 
#          "kitchen", 18.0,
#          "living room", 20.0,
#          "bedroom", 10.75,
#          "bathroom", 9.50]

# print (areas[1])
# print (areas[-1])
# print (areas[5])

# #########################

# SUBSET & CALCULATE
x = ["a", "b", "c", "d"]
print(x[1] + x[3])



areas = ["hallway", 11.25, 
         "kitchen", 18.0,
         "living room", 20.0,
         "bedroom", 10.75,
         "bathroom", 9.50]


# create a new variable, eat_sleep_area, that contains the sum
# of the area of the kitchen and the area of the bedroom.
eat_sleep_area = areas[3] + areas[7]
print (eat_sleep_area)


areas = ["hallway", 11.25, 
         "kitchen", 18.0,
         "living room", 20.0,
         "bedroom", 10.75,
         "bathroom", 9.50]

# create a list, downstairs, containing first 6 elements of areas.
downstairs = areas[:6]

# create a list, upstairs, containing last 4 elements of areas.
upstairs = areas[6:]

print (downstairs)
print (upstairs)
