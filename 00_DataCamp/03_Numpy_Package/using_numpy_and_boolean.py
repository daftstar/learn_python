import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

bmi = (np_weight / (np_height ** 2))
# print (bmi)

# print (bmi > 24)

# print all BMI values < 23
# print (bmi[bmi < 23])

# ####################################################
# COMPARE MULTIPLE CONDITIONS IN NUMPY ARRAY
# ####################################################

# Print Truth Statements
print (np.logical_and(bmi > 21, bmi < 22))

# Print Values within Truth Statements
print (bmi[np.logical_and(bmi > 21, bmi < 22)])
#


print ("\n________________________________________________________\n")




my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

print (my_house >= 18)
print (my_house < your_house)


# Which areas in my_house are greater than 18.5 or smaller than 10?
print (np.logical_or(my_house > 18.5, your_house < 10))



# Which areas are smaller than 11 in both my_house and your_house
print (np.logical_and(my_house < 11, your_house < 11))
