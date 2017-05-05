# ### THE OLD WAY OF DOING IT VIA LISTS:


# population = [20.44, 1.5, 40.82]
# countries = ["Albania", "Lichtenstein", "Belgium"]

# # access the location of the country Belgium within countries
# ind_belgium = countries.index("Belgium")

# # access the population of the Belgium using its index value
# pop_belgium = population[ind_belgium]

# # print (ind_belgium)
# # print (pop_belgium)


# # USING DICTIONARIES

# world = {
#         "Albania": 20.44,
#         "Lichtenstein": 1.5,
#         "Belgium": 40.82
#         }

# for key, value in world.items():
#     print ("%s - %s" % (key, value))


countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# USE DICTIONARY INSTEAD OF MULTIPLE LISTS
europe = {
            "spain": "madrid",
            "france": "paris",
            "germany": "berlin",
            "norway": "oslo"
            }

# Print out the keys in europe
print (europe.keys())

# Print out value that belongs to key 'norway'
print (europe["norway"])


# DICTIONARIES CANNOT BE EDITED ONCE THEY'VE BEEN CREATED > IMMUTABLE
# DICTIONARIES DO NOT MAINTAIN ORDER
# LISTS MAINTAIN ORDER

# Adding to Dictionaries is possible, as this is not editing the dict. 

europe["sealand"] = 0.00027
print (europe)
print (countries)

print ("sealand" in europe)

del europe["sealand"]
print ("sealand" in europe)



#           LISTS                              DICTIONARIES
#  select, Update and remove: []   |    select, Update and remove: []
#  Indexed by range of numbers     |    Indesxed by unique keys
#  Collection of values            |    Lookup table with unique keys
#    - order matters               |
#    - select entire subsets       |



   
