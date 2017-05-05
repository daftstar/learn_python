import pandas as pd
import numpy as np


# ########################################
# DATAFRAME INPUTS / IMPORT CSV
# ########################################

brics = pd.read_csv("country.csv")

# ########################################
# ASSIGN ROW LABLELS
# ########################################

row_labels = ['BR', 'RU', 'IN', 'CH', 'SA']
brics.index = row_labels

# print (brics)


# ____________________________

# Select countries with area > 9 mm km2
# Get column series, NOT data frame

# print (brics[["area"]])  # DATAFRAME
# print (brics["area"])

# can also be printed as
# print (brics.loc[:, "area"])
# print (brics.iloc[:, 2])

# CREATE VARIABLE THAT STORES SERIES 
is_huge = (brics["area"] > 8)
# print (is_huge)

# ONLY SHOW COUNTRIES is_huge is False
# print (brics[is_huge == False])


# ONLY SHOW COUNTRIES is_huge is True
# print (brics[is_huge])



# SHOW COUNTRIES WITH AREA > 8 AND < 10
mid = np.logical_and(brics["area"] > 8, brics["area"] < 10)
print (mid)
print ("\n")
print (brics[mid])
