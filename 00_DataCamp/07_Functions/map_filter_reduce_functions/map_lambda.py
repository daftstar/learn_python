# Map applies a function over an object, such as a list.

nums = [2, 4, 6, 8, 10]
result = map(lambda a: a ** 2, nums)

# print as a list, otherwise returns as a <map object at 0x102b34550>
print (list(result))


spells = ["protego", "accio", "expecto patronum", "legilimens"]
# use map() to apply lambda function over spells: shout_spells

# ####################################
# TRADITIONAL WAY
# ####################################


def shout_spells(item):
    shouted_spells_list = []
    for i in item:
        shouted_spells_list.append(i + "!!!")
    return shouted_spells_list


print (shout_spells(spells))

# ####################################
# MAP LAMBDA WAY
# ####################################


shout_spells = map(lambda item: item + "!!!", spells)
shout_spells_list = (list(shout_spells))
print (shout_spells_list)
