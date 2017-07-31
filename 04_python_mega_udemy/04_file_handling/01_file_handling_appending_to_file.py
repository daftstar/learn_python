# open file with write permissions
# note, a aloows to append.
# creates a new file called "a_new_file"


# r opens a file for read only. pointer is at beginning. 
# r+ opens file for read/write. pointer is at beginning.

# w opens a file for writing only. OVERWRITES file if it exists
#   Creates a new file if file does not exist
# w+ Opess file for read & write - OVERWRITES existing file.
#   Creates new file if file does not exist

# a opens file for appending. Pointer is at END of file if
# file already exists. Creates new file if file does not exist
# a+ opens file for appending and reading. 


file = open("a_new_file.txt", "a+")
# file.seek(0) # moves to beginning

content = file.readlines()
for i in content:
    print (i)

# print (content)
# file.write("hello world!")
# file.write("\n")

# for i in range(10):
#     file.write("Tomato %s\n" % i)
    
file.close()
