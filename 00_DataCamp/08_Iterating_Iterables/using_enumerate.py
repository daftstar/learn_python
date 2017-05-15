mutants = [
    'charles xavier',
    'bobby drake',
    'kurt wagner',
    'max eisenhardt',
    'kitty pride'
    ]

mutant_list = enumerate(mutants)
print (mutant_list)


# Unpack and print the tuple pairs
for index1, value1 in list(enumerate(mutants)):
    print (index1, value1)

# Change the start index
for index2, value2 in enumerate(mutant_list, start=1):
    print(index2, value2)

# ___________________________________________________

mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pride']
aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']
powers = ['telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility']

# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)
