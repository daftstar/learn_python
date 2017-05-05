
# this automates the open and close events by calling on 
# built in functions __enter__() and __exit__()
# f = open("hyy.txt")


with open("text.txt", "w") as my_file:
    my_file.write("Hey There!")

# TESTING FOR FILE CLOSE
print (my_file.closed)



if my_file.closed == False:
    my_file.close()
else:
    print ("File is closed")


# print (f.closed)

# f.close()
# print (f.closed)


