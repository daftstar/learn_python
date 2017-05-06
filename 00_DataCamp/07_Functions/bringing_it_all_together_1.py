# Bringing it all together
# campus.datacamp.com/courses/python-data-science-toolbox-part-1/writing-your-own-functions?ex=12

import pandas as pd


# Import twitter data as DataFrame
# tweets.csv is a large flat 100 row file containing
# general user information + recent tweets & retweets
df = pd.read_csv("tweets.csv")

# Column header names
# contributors, coordinates, created_at, entities, extended_entities,
# favorite_count, favorited, filter_level, geo, id, id_str,
# in_reply_to_screen_name, in_reply_to_status_id, in_reply_to_status_id_str
# in_reply_to_user_id, in_reply_to_user_id_str, is_quote_status
# lang, place, possibly_sensitive, quoted_status, quoted_status_id
# quoted_status_id_str, retweet_count, retweeted, retweeted_status
# source, text, timestamp_ms, truncated, user


# #########################################################
""" PART 1: Count how many times each language is used """
# #########################################################


# Initialize an empty dictionary: langs_count
langs_count = {}


# Extract column from DataFrame: col
col = df["lang"]


# Iterate over lang column within DataFrame
for entry in col:

    # If language is in langs_count dictionary, add 1:
    if entry in langs_count.keys():
        langs_count[entry] += 1

    # If language does not exist, add it and set value to 1    
    else:
        langs_count[entry] = 1


# Show values for dictionary: langs_count
for language, amount in langs_count.items():
    print ("language: %s - %s" % (language, amount))