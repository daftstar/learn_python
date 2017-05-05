def spacer():
    print ("\n_________________________________________________________________________\n")
    

# Putting data in a dictionary and then building a DataFrame works,
# but it's not very efficient.

import pandas as pd

# Import the cars.csv data: cars
abbrv = ["US", "AUS", "JP", "IN", "RU", "MO", "EG"]

cars = pd.read_csv("cars1.csv")

print (cars)
spacer()

######################################
# ACESS SPECIFIC COLUMNS OF DATAFRAME
#####################################
print (cars[["Country", "population"]])
spacer()


######################################
# ACESS SPECIFIC ROWS OF DATAFRAME
#####################################
print(cars[1:3])
spacer()

############################################
# ACESS SPECIFIC LOCATION WITHIN DATAFRAME - label based
############################################

# using row index value
print (cars.loc[[1]])
spacer()


# using column values as series
print (cars.loc[:, ["Country", "population"]])
spacer()


# # using Row & Column
# print (cars.loc[[0, 3, 2], ["Country", "country drives_right"]])
# spacer()


# # ____________________________________
# # USE iloc if you don't have column values
# # ____________________________________

# print (cars.iloc[[1]])
# spacer()

# #            rows: 0,2,3.  cols: 0, 1 
# print (cars.iloc[[0,2,3], [0,1]])
