import pandas as pd

# assign the contents of cars.csv to variable cars (no index column)
cars = pd.read_csv("cars.csv", index_col=0)

# Extract drives_right column as Series: dr
# then use dr, a boolean Series, to subset the cars DataFrame.
#  Store the resulting selection in sel.
print (cars)


dr = (cars["drives_right"])
sel = cars[dr]

print (sel)
print ("\n\n")

# OR, CONVERTED TO 1 LINE:

sel = cars[cars["drives_right"]]
print (sel)
