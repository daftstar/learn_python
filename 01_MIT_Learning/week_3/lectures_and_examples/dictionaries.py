animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
animals['d'] = 'donkey'

# # print key only
# for key in animals:
#     print (key)

# print key & value
for key, value in animals.items():
    print (key + ": " +  value)

print (animals)
print (animals['c'])
# print (animals['donkey'])

print (len(animals))

animals['a'] = 'anteater'
print (animals['a'])


print (len(animals['a'])) # FALSE


# See if donkey exists within dictionary values
print ('donkey' in animals.values())    # TRUE

print ('b' in animals)

print (animals.keys())

del animals['b']
print (animals)


print ('donkey' in (animals.values()))

