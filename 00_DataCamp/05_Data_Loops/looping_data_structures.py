# _________________________________________________
# #### DICTIONARIES VS NUMPY ARRAYS ####

# ### DICTIONARIES REQUIRE METHOD FOR ITERATION 
#   for key, val in my_dict.items():
#       print (key, val)


# ### NUMPY ARRAYS REQUIRE FUNCTIONS
#   for val in np.diter(my_array):
        # print (val)
# ___________________________________________________



world = {
    "albania": 2.77,
    "algeria": 39.21,
    "amazonia": 99.33
}

# To loop through data structures, call method items()

for i, x in world.items():
    print(i, x)

# USING NUMPY

import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / (np_height ** 2)
meas = np.array([np_height, np_weight])

# to iterate through a numpy array, you use regular for expressions
for val in bmi:   # bmi = numpy array
    print (val)


# to iterate through a 2D numpy array (meas), use .nditer()
for i in np.nditer(meas):
    print (i)


