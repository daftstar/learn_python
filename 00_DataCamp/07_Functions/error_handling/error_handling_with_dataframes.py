import pandas as pd

tweets_df = pd.read_csv("tweets.csv")

# ########################################################
# STEP 1: write a lambda function and use filter()
# to select retweets, that is, tweets that begin with
# string 'RT'
#
# lambda function should check if the first 2 characters
# in tweet x are 'RT'

# ########################################################


# ########################################################
# Traditional method way
# ########################################################

def getRT(dataframe_file):
    result = []
    for i in dataframe_file:
#       if first two letters are 'RT'
        if i[0:2] == "RT":
            result.append(i)
    list_result = list(result)
    return (list_result)


result2 = (getRT(tweets_df['text']))

for i in result2:
    print (i)

print ("\n___________________________________________________\n")


# ########################################################
# Lambda Filter method way
# ########################################################


#                   1st two chars = 'RT'  data_frame['column name']
result = filter(lambda dataframe_file: dataframe_file[0:2] == 'RT', tweets_df['text'])
res_list = list(result)

# print each tweet
for i in res_list:
    print (i)

print ("\n___________________________________________________\n")


# ########################################################
# Methods with Try / Except Blocks
# ########################################################


def count_entries(df, col_name='lang'):
    """returns dictionary with counts of occurences
    as a value for each key """
    cols_count = []

    try:
        col = df[col_name]

        for entry in col:
            if entry in cols_count.keys():
                cols_count[entry] += 1
            else:
                cols_count[entry] = 1
        return cols_count
    except:
        print ('the DataFrame does not have a ' + col_name + ' column')

result1 = count_entries(tweets_df, 'lang')
result2 = count_entries(tweets_df, 'lang1')
print ("\n___________________________________________________\n")


# ########################################################
# Methods with ValueError Blocks
# ########################################################


# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]

    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

        # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df)


# Print result1
print(result1)

