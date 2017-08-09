import pandas as pd

# with no column or row names
df1 = pd.DataFrame([[2, 4, 6], [10, 20, 30]])
# print (df1)

# with no row names
df2 = pd.DataFrame(
    [[2, 4, 6], [10, 20, 30]],
    columns=["price", "age", "value"])
# print (df2)

# WITH ROW & COLUMN names
df3 = pd.DataFrame(
    [[2, 4, 6], [10, 20, 30]],
    columns=["price", "age", "value"],
    index=["First", "Second"])
# print (df3)


# PASSING DICTIONARIES
df4 = pd.DataFrame(
    [{"Name": "John"},
     {"Name": "Jack"}]
    #  index=["First", "Second"]
)
print (df4)
