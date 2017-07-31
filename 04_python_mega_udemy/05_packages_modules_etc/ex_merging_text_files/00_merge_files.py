# Use a "with" statement to create a new text file and
# iterate through the file list inside that "with" statement
# and open and read existing file contents in each iteration
# and write them to new text file.

# import os commands
import os
import datetime


def merge_files():
    # list all files in directory
    # print(os.listdir())
    all_files = (os.listdir())

    # create filename
    now = (datetime.datetime.now())
    pleasant_time = now.strftime("%a %b %y (%H-%M-%S)") # http://strftime.org
    pleasant_filename = pleasant_time

    # Searching for all .txt files
    for file in all_files:
        if file.endswith(".txt"):
            txt_file = open(file, "r")
            contents = txt_file.readlines()

            with open(str(pleasant_filename)+".txt", "a+") as file:
                for line in contents:
                    file.write(line + "\n")

            txt_file.close()

    return ("complete")

print (merge_files())