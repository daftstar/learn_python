import pandas as pd
new_line = "\n_____________________________\n"

# Import CSV spreadsheet using pandas
cars = pd.read_csv("cars.csv", index_col=0)


# ########################
# Loop over DataFrame (1)
# ########################

# ITERATE THROUGH ROWS (print row label and row contents)
# for lab, row in cars.iterrows():
#     print (lab)
#     print (row)


# ########################
# Loop over DataFrame (2)
# ########################

# Add description to string printouts
# for lab, row in cars.iterrows():
#     print ("%s: %s" % (lab, row["cars_per_cap"]))


# ########################
# Add Column (1) - INEFFICIENTLY add column COUNTRY
# ########################

for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()


# ########################
# Add Column (2) - EFFICIENTLY add column COUNTRY
# ########################

cars["COUNTRY"] = cars["country"].apply(str.upper)
print (cars)
