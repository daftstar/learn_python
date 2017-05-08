import pandas as pd
tweets_df = pd.read_csv("tweets.csv")

# #####################################################
# CREATE A FUNCITON W/ SINGLE DEFAULT VAL THAT OUTPUTS:
# dictionary with counts of occurrences # of each
# language used in tweets.csv using 1 default value
# #####################################################


def count_entries(df, column_name="lang"):
    """ Return a dictionary with counts of
    occurrences as value for each key """

    # Initialize empty dictionary
    cols_count = {}

    # Extract column namefrom DataFrame: col
    col = df[column_name]

    # Iterate over the column in the DataFrame
    for entry in col:
        if entry in cols_count.keys():   # if entry exists
            cols_count[entry] += 1   # increment counter by 1
        else:   # add entry to cols_count and set val to 1
            cols_count[entry] = 1

    return (cols_count)


result1 = count_entries(tweets_df)
result2 = count_entries(tweets_df, "source")

print (result1)
# print (result2)

# ____________________________________________________________


# #####################################################
# CREATE A FUNCITON W/ FLEX DEFAULT VAL THAT OUTPUTS:
# dictionary with counts of occurrences # of each
# language used in tweets.csv using 1 default value
# #####################################################


def count_entries(df, *args):
    """ Return a dictionary with counts of
    occurrences as value for each key """

    cols_count = {}

    for column_name in args:
        col = df[column_name]

        for entry in col:
            if entry in cols_count.keys():
                cols_count[entry] += 1
            else:
                cols_count[entry] = 1
    return (cols_count)


result1 = count_entries(tweets_df, "lang")
result2 = count_entries(tweets_df, "lang", "source")

print (result1)