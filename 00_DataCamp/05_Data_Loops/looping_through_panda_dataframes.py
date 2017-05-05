import pandas as pd

#import CSV spreadsheet using pandas
new_line = "\n_____________________________\n"
cars = pd.read_csv("cars.csv", index_col=0)

print (new_line)

# THIS PRINTS OUT COLUMN NAMES ONLY
# for i in cars:
#     print (i)

# IN PANDAS, EXPLICITLY CALL OUT ITERATION OVER ROWS
# for lab, row in cars.iterrows():
#     print (lab)
#     print (row)


# PRINT SPECIFIC ITEMS IN DATAFRAME

for lab, row in cars.iterrows():
    print ("%s: %s" % (lab, row["country"]))
    # print (lab + ": " + row["country"])   # alternative method
print (new_line)

# Adding new columns to DataFrame >> this does NOT write to file
# This method is not efficient >> creating series on every iteration

for lab, row in cars.iterrows():
    cars.loc[lab, "name_length"] = len(row["country"])
print (cars)


print (new_line)

# TO EFFICIENTLY ADD NEW COLUMN TO DATAFRAME:
cars["name_length"] = cars["country"].apply(len)
print (cars)

