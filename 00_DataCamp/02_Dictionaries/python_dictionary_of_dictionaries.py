# DICTIONARY WITHIN DICTIONARY

# #####################################################################

#           LISTS                              DICTIONARIES
#  select, Update and remove: []   |    select, Update and remove: []
#  Indexed by range of numbers     |    Indesxed by unique keys
#  Collection of values            |    Lookup table with unique keys
#    - order matters               |
#    - select entire subsets       |


# #####################################################################


europe = {
    "spain": {    # key
        "capital": "madrid",   # value 1
        "population": 46.77    # value 2
    },
    "france": {
        "capital": "paris",
        "population": 66.03
    },
    "germany": {
        "capital": "berlin",
        "population": 80.62,
    },
    "norway": {
        "capital": "oslo",
        "population": 5.084
    }
}


# Get population of of spain within europe
pop_spain = (europe['spain']['population'])
print (pop_spain)

# print capital of france
print (europe['france']['capital'])


# create sub-dictionary called "data"
data = {
        "capital": "rome",
        "population": 59.83
        }


# add data to europe under key italy
europe["italy"] = data
print (europe)