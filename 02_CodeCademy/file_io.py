# deletes the contents of the file
my_file = open("output.txt", "w").close()

# creating variable my_file that allows for read & write
my_file = open("output.txt", "r+")


# creates array of i ** 2
my_list = [i ** 2 for i in range(1, 11)]

# write contents of array to file
for i in my_list:
    my_file.write(str(i) + "\n")  # convert to string to allow write


# close file so Python can finish writing to file.
my_file.close()

# read from output.txt
my_file = open("output.txt", "r")

# print all contents of file to console
print (my_file.read())

# close the file
my_file.close()


# Print each individual line of output.txt
my_file = open("output.txt", "r")
for i in my_file:
    print (my_file.readline())
my_file.close()








