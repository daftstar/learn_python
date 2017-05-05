# INSTRUCTIONS: 
# Within the CSV "Cars.csv", identify the countries that have cpc > 500


# import pandas library
import pandas as pd


# import and assign the contents of cars.csv to variable cars (no index column)
cars = pd.read_csv("cars.csv", index_col=0)


# Identify countries with cars_per_cap > 500
# # STEP 1: Select cars_per_cap column as panda series
cpc = cars["cars_per_cap"]
print (cpc)

# # STEP 2: use cpc w/ comparison operatior to boolean pop > 500
many_cars = cpc > 500
print (many_cars)

# # STEP 3: use many_cars to subset cars, store result as car_maniac

car_maniac = cars[many_cars]
print (car_maniac)
