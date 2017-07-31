# import os commands
import os

# print(dir(os)) # all os methods

# list all files in directory

# print(os.listdir())
all_files = (os.listdir())

for index, file in enumerate(all_files, 1):
    print (index," ", file)


print (os.__file__) #Users/nikhildaftary/anaconda/lib/python3.5/os.py