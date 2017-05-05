# numpy can only house data with the same data type. 
# to handle multiple types of data, use pandas


import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]  # drive left, drive right
cpc = [809, 731, 588, 18, 200, 70, 45]   # cars per capita


# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {
    "country": names,
    "drives_right": dr,
    "cars_per_cap": cpc
}

# build DataFrame cars from my_dict: cars

cars = pd.DataFrame(my_dict)
print (cars)