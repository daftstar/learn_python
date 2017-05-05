inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']


"""

1. Add a key to inventory called 'pocket'
2. Set the value of 'pocket' to be a list consisting of the strings
    'seashell', 'strange berry', and 'lint'
3. .sort() the items in the list stored under the 'backpack' key
4. Then .remove('dagger') from list of items stored under the 'backpack' key
5. Add 50 to the number stored under the 'gold' key

"""


# step 1 & 2:
inventory["pocket"] = ["seashell", "strange berry", "lint"]
inventory['pocket'].sort()


# step 3 - sort keys in backpack
inventory['backpack'].sort() 


# step 4 - remove dagger
# inventory["backpack".remove("dagger")]
inventory["backpack"].remove("dagger")


# step 5 - add 50 to gold
inventory["gold"] = inventory["gold"] + 50


# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 


print (inventory["pouch"])
print (inventory["pouch"][0])


