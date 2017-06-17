str1 = 'exterminate!' 
str2 = 'number one - the larch'

print (str1.upper())

print (str1.isupper())






str2 = str2.capitalize()
print (str2.index('n'))
print ()
print (str2.swapcase())

print (str2.index('e'))
print (str2.find('e'))

# print (str2.index('!'))

print (str2.find('!'))      # find returns -1 if value is not found
print (str1.count('e'))

print ()
str1 = str1.replace('e', '*')

print (str1)
print (str2.replace('one', 'seven'))


