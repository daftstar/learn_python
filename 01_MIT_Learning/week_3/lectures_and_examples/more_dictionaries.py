animals = {
        'a': ['aardvark'],
        'b': ['baboon'],
        'c': ['coati'],
        'd': ['donkey', 'dog', 'dingo']
        }


# Return the sum of the number of values associated
# with a dictionary. For example: print(how_many(animals)) = 6


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for i in aDict.values():
        count += len(i)
    return (count)


# print(how_many(animals))
# print ()

# Return the key corresponding to the entry with the largest
# number of values associated to it. If there is more than one
# such entry, return any one of the matching keys.
# For example, biggest(animals) returns 'd'



def biggest(aDict):
    result = None
    biggest = 0

    for key in aDict:
        if len(aDict[key]) > biggest:
            result = key
            biggest = len(aDict[key])

    return (result)
print (biggest(animals))




# ANOTHER WAY OF biggest :: LESS EFFICIENCT

# def biggest(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.

#     returns: The key with the largest number of values associated with it
#     '''
#     myDict = {}         # {lyric, instance}
#     best = len(max(aDict.values()))
#     # print (best)

#     for key, value in aDict.items():   
#         if len(value) == best:
#             myDict[key] = value

#     for i in myDict:
#         return i

# print (biggest(animals))








# ANOTHER WAY OF how_many :: LESS EFFICIENCT
# def how_many(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.
#     returns: int, how many values are in the dictionary.
#     '''
#     count = 0

#     for a, b in aDict.items():
#         for i in b:
#             count += 1

#     return (count)





