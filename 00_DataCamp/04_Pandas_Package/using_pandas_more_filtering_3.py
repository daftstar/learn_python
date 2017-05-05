# Use pandas for file import and string filtering + numpy for int filtering
import pandas as pd
import numpy as np

cars = pd.read_csv("cars.csv", index_col=0)

# Create dataframe, medium, that includes all cars with cars_per_cap
# between 100 and 500

# STEP 1: subset cars_per_cap column
cpc = cars["cars_per_cap"]
print (cpc)


# STEP 2: identify countries that meet requirements

between = np.logical_and(cpc > 100, cpc < 500)
print (between)


# STEP 3: Show entire dataframe observations of qualifiying countries

medium = cars[between]
print (medium)
