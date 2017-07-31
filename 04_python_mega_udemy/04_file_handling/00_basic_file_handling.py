file = open("example.txt", 'r')

content = file.read()
print (type(content))
print (content)
print ("________________________________")

# because the pointer is already at the end of the file,
# from the above, set pointer back to position 0
file.seek(0)

content=file.readlines()    # add lines to list
print (content)
print ()


content = [i.rstrip("\n") for i in content]


print (content)
for i in content:
    print (i)

# close the file so changes are saved - and so file can be
# accessed by another program

file.close()
