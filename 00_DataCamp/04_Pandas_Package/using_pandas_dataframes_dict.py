import pandas as pd

# ########################################
# DATAFRAME INPUTS
# ########################################

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]  # drive left, drive right
cpc = [809, 731, 588, 18, 200, 70, 45]   # cars per capita


# ########################################
# DICTIONARY FOR DATAFRAME
# ########################################

dict = {
    "country": names,     # column header w/ names
    "drives_right": dr,	  # column header w/ names
    "cars_per_cap": cpc   # column header w/ names
}


# ########################################
# DATA FRAME DEFINE, BUILD, DISPLAY
# ########################################

# build DataFrame cars from my_dict: cars
cars = pd.DataFrame(dict)

# Define row labels:
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']
cars.index = row_labels

print (cars)
