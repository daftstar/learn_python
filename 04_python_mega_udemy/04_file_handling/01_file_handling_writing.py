# open file with write permissions
# note, w is not an append.
# creates a new file called "a_new_file"
file = open("a_new_file.txt", "w")

# content = file.readlines()
file.write("hello world!")
file.write("\n")

for i in range(10):
    file.write("Line %s\n" % i)
    
file.close()
