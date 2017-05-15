def newline():
    print ("\n__________________________________\n")


avengers = ['hawkeye', 'ironman', 'thor', 'quicksilver']
names = ['barton', 'stark', 'odinson', 'maximoff']




values = range(10,21)
values_list = list(values)

print (values_list)

values_sum = sum(values)
print (values_sum)
newline()

# ####################################################
# USING ENUMERATE
# ####################################################
avengers = ['hawkeye', 'ironman', 'thor', 'quicksilver']
e = enumerate(avengers)


# print contents of enumerate object e
print (list(e))

for index, value in enumerate(avengers):
    print (index, value)


# change index start number
for index, value in enumerate(avengers, start=10):
    print (index, value)

newline()



# ####################################################
# USING ZIP
# ####################################################

# merge two lists together
z = zip(avengers, names)
print (type(z))     # <class 'zip'>

# convert zip object to list
z_list = list(z)
print(z_list)

for i in z_list:
    print (i)

print (*z_list)





